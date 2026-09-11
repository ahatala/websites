"""Generate the static GitHub Pages site: python3 build.py (no dependencies)."""
from pathlib import Path
from collections import defaultdict
from html import escape as esc
from urllib.parse import quote
from math import ceil
import json
from menu import CAT, RECIPES
from shopping import FI, PRODUCTS, PACKS, STORE
from translations_fi import localize, DAYS as DAY_NAMES, KINDS as KIND_NAMES, SHOP_NOTES as NOTES
localize(CAT, RECIPES)
ROOT=Path(__file__).parent
DAYS=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
ORDER={'Breakfast':0,'Lunch':1,'Lunch / snack':1,'Dinner':2,'Dessert':3}
WEEKS={
'greece':dict(name='Kreikka',number=1,tag='Viikon ruokalista',desc='Kuusi päivällistä sekä sunnuntain lounas ja jälkiruoka. Lauantaina ei valmisteta ruokaa.',heads='Yleensä 4 annosta · torstaina 3 · lauantai vapaa',prep=['Tarkista filotaikinan sulatusohje ennen tiistaita. Varaa riittävästi sunnuntain piiraaseen ja noudata pakkauksen säilytysohjetta.','Torstain giouvetsi vaatii pitkän haudutuksen. Aloita ajoissa tai hauduta liha etukäteen.','Valmista sunnuntain moussakan liha- ja kasvistäytteet rinnakkain. Lounaaksi on tiropitaa ja jälkiruoaksi hunajamunkkeja.']),
'uk':dict(name='Britannia',number=2,tag='Viikon ruokalista',desc='Maanantaina tikka masalaa, torstaina fish & chips ja sunnuntaina kukkakaaligratiinia lisukkeineen.',heads='Ma–pe 4 annosta · viikonloppuna 3',prep=['Viikonloppuna ruokailijoita on kolme: kaksi lihansyöjää ja yksi kasvissyöjä. Kaikki viikonlopun reseptit on mitoitettu kolmelle.','Fish & chips on torstaina. Perjantain makkarapannukakku tehdään kahteen vuokaan, joista pienemmässä on kasvismakkaraa.','Sunnuntain kukkakaaligratiini on kaikille. Reseptissä on mukana perunat, Yorkshire-vanukkaat, kasvikset ja sipulikastike.']),
'china':dict(name='Kiina',number=3,tag='Viikon ruokalista',desc='Wokkiruokia, itse tehtyjä jiaozi-nyyttejä ja sunnuntain hot pot. Chili tarjoillaan erikseen.',heads='4 annosta päivittäin · tarvittaessa 3 liha- ja 1 kasvisannos',prep=['Perjantain nyyttikuoret tehdään vehnäjauhoista. Taittele sieninyytit ensin ja anna niille eri muoto kuin lihaversiolle.','Lauantain mangovanukkaat tarvitsevat kolme tuntia jääkaapissa. Sunnuntain jälkiruokana on seesamikeksejä ja jäätelöä.','Hot potissa käytetään yhteistä kasviskattilaa ja erillistä lihakattilaa. Molemmat voi pitää myös liedellä.'])}


def qfmt(q):
    if q==int(q): return str(int(q))
    return f'{q:g}'
def amount(key,q):
    unit=CAT[key]['unit']
    value=qfmt(q).replace('.', ',')
    if unit=='tsp': value={0.25:'¼',0.5:'½',0.75:'¾',1.5:'1½'}.get(q,value)
    unit={'whole':'kpl','pieces':'kpl','tsp':'tl','g drained':'g valutettuna','ml prepared':'ml valmista lientä'}.get(unit,unit)
    return f'{value} {unit}'
def sum_week(week):
    totals=defaultdict(float); uses=defaultdict(list)
    for r in RECIPES:
        if r['week']==week:
            for i in r['ingredients']:
                totals[i['key']]+=i['qty']; uses[i['key']].append((r,i['qty']))
    return totals,uses

def shell(title,body,week='',prefix=''):
    nav=''.join(f'<a href="{prefix}{w}.html"'+(' aria-current="page"' if week==w else '')+f'>{esc(v["name"])}</a>' for w,v in WEEKS.items())
    return f'''<!doctype html><html lang="fi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#203c33"><meta name="description" content="Perheen ruokaviikot: Kreikan, Britannian ja Kiinan ruokalistat, reseptit ja ostoslistat."><title>{esc(title)} · Perheen ruokaviikot</title><link rel="icon" href="{prefix}assets/greece.svg" type="image/svg+xml"><link rel="stylesheet" href="{prefix}assets/style.css"><script src="{prefix}assets/app.js" defer></script></head><body class="{week}" id="top"><a class="skip" href="#main">Siirry sisältöön</a><header class="site-header"><div class="wrap header-inner"><a class="brand" href="{prefix}index.html"><span class="brand-mark" aria-hidden="true">r</span><span>PERHEEN<br>RUOKAVIIKOT</span></a><nav class="nav" aria-label="Maiden ruokalistat">{nav}</nav></div></header><main id="main">{body}</main><footer class="footer"><div class="wrap footer-inner"><p>Perheen ruokaviikot · Kreikka, Britannia ja Kiina<br><span class="image-credit">Ruokakuvitukset on luotu tekoälyllä.</span></p><a href="{prefix}index.html#our-table">Ruokavaliot ja annosmäärät</a><a href="#top">Takaisin alkuun ↑</a></div></footer></body></html>'''

def write(path,content):
    target=ROOT/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(content)

def recipe_link(r,prefix=''):
    return f'{prefix}recipes/{r["id"]}.html'

HERO_DISHES={'greece':'souvlaki','uk':'fish-chips','china':'hot-pot'}

def dish_image(id, prefix='', *, alt='', eager=False, sizes='(max-width: 650px) 90vw, 560px'):
    base=f'{prefix}assets/dishes/{id}'
    loading='loading="eager" fetchpriority="high"' if eager else 'loading="lazy"'
    return f'<img class="dish-image" src="{base}-small.jpg" srcset="{base}-small.jpg 480w, {base}.jpg 1200w" sizes="{sizes}" width="1200" height="800" alt="{esc(alt)}" {loading} decoding="async">'

def home_collage():
    return '<div class="food-collage">'+''.join(f'<a class="food-postcard postcard-{w}" href="{w}.html">{dish_image(HERO_DISHES[w], eager=w=="greece", sizes="(max-width: 650px) 65vw, 380px")}<span>{v["name"]}</span></a>' for w,v in WEEKS.items())+'</div>'

def homepage():
    cards=''
    for w,v in WEEKS.items():
        dinners=sum(r['week']==w and r['kind']=='Dinner' for r in RECIPES)
        cards+=f'''<article class="country-card {w}" id="{w}"><div class="card-art">{dish_image(HERO_DISHES[w], sizes="(max-width: 650px) 90vw, 380px")}</div><div class="card-body"><span class="eyebrow">Viikko {v['number']} · {dinners} päivällistä</span><h3>{v['name']}</h3><p>{v['heads']}.</p><a class="card-link" href="{w}.html">Avaa ruokalista</a></div></article>'''
    body=f'''<div class="wrap"><section class="hero"><div><span class="eyebrow">Kreikka · Britannia · Kiina</span><h1>Kolmen maan<br>ruokaviikot</h1><p class="intro">Perheen kolmen viikon ruokalista, reseptit ja viikoittaiset ostoslistat K-Citymarket Ruoholahteen.</p><div class="actions"><a class="button" href="#weeks">Valitse viikko <span aria-hidden="true">↓</span></a><a class="button secondary" href="#our-table">Ruokavaliot ja annokset</a></div></div>{home_collage()}</section></div><div class="ribbon"><div class="wrap"><span>20 päivällistä + 10 muuta ateriaa</span><span>Ei maapähkinää · Ei lohta</span><span>K-Citymarket Helsinki Ruoholahti</span></div></div><div class="wrap"><section class="section" id="weeks"><div class="section-head"><div><span class="eyebrow">Ruokalistat</span><h2>Valitse viikko</h2></div><p>Ostoslistat sisältävät myös lisukkeet, jälkiruoat ja erikseen valmistettavat kasvisannokset.</p></div><div class="countries">{cards}</div></section><section class="section" id="our-table"><span class="eyebrow">Suunnitelman lähtökohdat</span><h2>Ruokavaliot ja annosmäärät</h2><div class="rules"><div><span class="rule-num">01 / Ainekset</span><h3>Ei maapähkinää eikä lohta</h3><p>Resepteissä ei käytetä maapähkinää, maapähkinäöljyä, lohta eikä muuta punalihaista kalaa. ”Saattaa sisältää maapähkinää” sopii tälle perheelle. Kala-ateriaan käytetään turskaa tai koljaa.</p></div><div><span class="rule-num">02 / Annokset</span><h3>Yleensä neljälle</h3><p>Yleensä kolme lihansyöjää ja yksi lihaa ja siipikarjaa välttävä ruokailija. Kala, kananmunat ja maitotuotteet sopivat hänelle. Tarvittaessa yksi annos valmistetaan erikseen; lisukkeet ovat yhteiset.</p></div><div><span class="rule-num">03 / Ostokset</span><h3>K-Citymarket Ruoholahti</h3><p><a href="{STORE}">K-Citymarket Helsinki Ruoholahti</a> on ostoslistojen lähtökohta. Listoissa on K-Ruoan hakulinkit, tuote-esimerkkejä ja korvaavia aineksia.</p></div></div><p class="small" style="margin-top:16px">Määrät on laskettu tavallisille aikuisten annoksille; sovita ne ruokahaluun. Listat kattavat vain tässä suunnitellut ateriat. Valitse K-Ruoassa Ruoholahti ja tarkista tuotteiden saatavuus sekä ainesosat.</p></section><section class="section" id="scorecard"><div class="section-head"><div><span class="eyebrow">Arviointi</span><h2>Perheen suosikit</h2></div><p>Kirjatkaa suosikit, kun olette kokeilleet ruokia.</p></div><div class="score-grid"><div class="score-item"><label for="best-dish">Paras ruoka</label><input id="best-dish" data-save="best-dish" placeholder="Ruoan nimi"></div><div class="score-item"><label for="best-dessert">Paras jälkiruoka</label><input id="best-dessert" data-save="best-dessert" placeholder="Jälkiruoan nimi"></div><div class="score-item"><label for="surprise">Suurin yllätys</label><input id="surprise" data-save="surprise" placeholder="Ruoka tai kokemus"></div><div class="score-item"><label for="winning-country">Suosikkimaa</label><select id="winning-country" data-save="winning-country"><option value="">Valitse maa</option><option value="Greece">Kreikka</option><option value="United Kingdom">Britannia</option><option value="China">Kiina</option></select></div></div><p class="small" style="margin-top:12px">Vastaukset tallentuvat tähän selaimeen. Ne eivät siirry laitteiden välillä.</p></section></div>'''
    write(Path('index.html'),shell('Kolmen maan ruokaviikot',body))

def country(week,v):
    days=''
    for day in DAYS:
        rs=sorted([r for r in RECIPES if r['week']==week and r['day']==day],key=lambda r:ORDER[r['kind']])
        if not rs:
            days+=f'<article class="day skipped"><div class="day-name">{DAY_NAMES[day]}<span>Ei aterioita</span></div><div><h3>Vapaapäivä</h3><p class="small">Lauantaille ei ole suunniteltu aterioita eikä ostoksia.</p></div></article>';continue
        meals=''
        for r in rs:
            meals+=f'''<div class="meal"><a class="meal-image" href="{recipe_link(r)}" aria-label="{esc(r['title'])}: resepti">{dish_image(r['id'], sizes="(max-width: 650px) 85vw, 230px")}</a><div class="meal-copy"><span class="eyebrow">{KIND_NAMES[r['kind']]}</span><h3><a href="{recipe_link(r)}">{esc(r['title'])} ↗</a></h3><p>{esc(r['desc'])}</p><div class="meta"><span class="pill">{esc(r['split'])}</span><span>{esc(r['time'])}</span></div></div></div>'''
        days+=f'<article class="day"><div class="day-name">{DAY_NAMES[day]}<span>{rs[0]["servings"]} ruokailijaa</span></div><div>{meals}</div></article>'
    prep=''.join(f'<li>{esc(p)}</li>' for p in v['prep'])
    body=f'''<div class="wrap"><section class="hero"><div><span class="eyebrow">Viikko {v['number']}</span><h1>{v['name']}</h1><p class="intro">{v['desc']}</p><p class="pill">{v['heads']}</p><div class="actions"><a class="button" href="{week}-shopping.html">Viikon ostoslista ↗</a><a class="button secondary" href="#menu">Ruokalista ↓</a></div></div><div class="hero-art country-photo">{dish_image(HERO_DISHES[week], alt=v['name']+': ruokakuvitus', eager=True)}<div class="stamp"><b>0{v['number']}</b>viikko</div></div></section><nav class="subnav" aria-label="Viikon sisältö"><a href="#menu">Ruokalista</a><a href="{week}-shopping.html">Ostoslista</a><a href="#kitchen-notes">Huomioita</a></nav><section class="section" id="menu"><div class="section-head"><div><span class="eyebrow">Päiväkohtainen suunnitelma</span><h2>Ruokalista</h2></div><p>Avaa resepti ruoan nimestä. Ohjeessa ovat ainekset, valmistus ja mahdollinen kasvisversio.</p></div><div class="week-layout"><div class="days">{days}</div><aside class="aside" id="kitchen-notes"><div><h3>Ennen ruoanlaittoa</h3><ul>{prep}</ul></div><div><a class="button" href="{week}-shopping.html">Avaa ostoslista</a><p class="small" style="margin-top:15px">Sisältää kaikki suunnitellut ateriat, myös mausteet ja kasvisannosten ainekset.</p></div></aside></div></section></div>'''
    write(Path(f'{week}.html'),shell(v['name'],body,week))

def recipe(r):
    week=r['week'];v=WEEKS[week]
    items=''.join(f'<li><span>{esc(CAT[i["key"]]["label"])}</span><span class="quantity">{amount(i["key"],i["qty"])}</span></li>' for i in r['ingredients'])
    steps=''.join(f'<li>{esc(s)}</li>' for s in r['steps'])
    note=f'<div class="note"><strong>Huomio</strong><p>{esc(r["note"])}</p></div>' if r['note'] else ''
    oven_note='<p class="small">Lämpötilat ovat kiertoilmauunille. Käytä tavallisessa uunissa noin 20 °C korkeampaa lämpötilaa.</p>' if any('uuni' in step or 'uunin' in step for step in r['steps']) else ''
    source=''
    if r['id']=='hot-pot': source='<p class="small">Lisätietoa valmistelusta: <a href="https://thewoksoflife.com/chinese-hot-pot-at-home/">The Woks of Lifen hot pot -opas (englanniksi)</a>. Käytä kuitenkin tämän reseptin aineksia ja erillistä lihakattilaa.</p>'
    body=f'''<div class="wrap"><header class="recipe-top"><div class="recipe-intro"><a class="crumb" href="../{week}.html#menu">← Viikko {v['number']} · {v['name']}</a><p class="eyebrow" style="margin-top:22px">{DAY_NAMES[r['day']]} / {KIND_NAMES[r['kind']]}</p><h1>{esc(r['title'])}</h1><p class="desc">{esc(r['desc'])}</p><div class="meta"><span class="pill">{r['servings']} annosta</span><span class="pill">{esc(r['split'])}</span><span class="pill">{esc(r['time'])}</span></div><div class="actions"><button class="button" data-print>Tulosta resepti</button><a class="button secondary" href="../{week}-shopping.html">Viikon ostoslista</a></div></div><figure class="recipe-photo">{dish_image(r['id'], '../', alt='Kuvitus: '+r['title'], eager=True)}</figure></header><div class="recipe-layout"><section class="ingredients"><h2>Ainekset</h2><p class="small">Määrät yhteensä {r['servings']} annokseen, myös lisukkeisiin ja mahdolliseen kasvisversioon. Vesi mainitaan valmistusohjeessa.</p><ul>{items}</ul></section><section class="method"><h2>Valmistus</h2>{oven_note}<ol class="steps">{steps}</ol>{note}{source}<p class="small" style="margin-top:20px">Kypsymisaika riippuu laitteista ja ainesten koosta. <a href="https://www.gov.uk/food-hygiene-businesses/cooking">Kypsennysohjeet (englanniksi)</a>: tarkista ohjeessa mainittu sisälämpötila puhtaalla paistomittarilla.</p></section></div><nav class="recipe-links" aria-label="Reseptin navigaatio"><a href="../{week}.html#menu">← Takaisin ruokalistaan</a><a href="../{week}-shopping.html">Viikon ostoslista →</a></nav></div>'''
    write(Path('recipes')/f'{r["id"]}.html',shell(r['title'],body,week,'../'))

def buying(key,qty):
    if key in PACKS:
        size=PACKS[key];n=ceil(round(qty/size,8))
        return f'Pakkausesimerkki: {n} × {amount(key,size)}. Vähennä kotona jo oleva määrä.'
    if key=='stock':return f'Kuutioita tai tiivistettä {qfmt(qty/1000).replace(".", ",")} litraan valmista lientä.'
    if key=='lemon':return f'Osta vähintään {ceil(qty)} sitruunaa.'
    if key=='garlic':return f'Noin {ceil(qty/8)} kokonaista valkosipulia ({ceil(qty)} kynttä).'
    return ''


def shopping(week,v):
    totals,uses=sum_week(week);groups=defaultdict(list)
    for key in sorted(totals,key=lambda k:CAT[k]['label']):groups[CAT[key]['group']].append(key)
    text_lines=[f'PERHEEN RUOKAVIIKOT — VIIKKO {v["number"]}: {v["name"].upper()}',v['heads'],'K-Citymarket Helsinki Ruoholahti','Kaikki suunnitellut ateriat, lisukkeet ja erilliset annokset. Vähennä määristä kotona jo olevat ainekset.','Ei maapähkinää eikä lohta. Saattaa sisältää maapähkinää -merkintä sopii.','']
    grid=''
    for group in dict.fromkeys(CAT[k]['group'] for k in CAT):
        if group not in groups:continue
        items='';text_lines.append(group.upper())
        for key in groups[group]:
            qty=totals[key];cat=CAT[key];fi=FI[key];search=f'https://www.k-ruoka.fi/kauppa/tuotehaku?haku={quote(fi)}'
            buy=buying(key,qty);detail=f'<p>{esc(buy)}</p>' if buy else ''
            if key in NOTES:detail+=f'<p>{esc(NOTES[key])}</p>'
            detail+=f'<a href="{search}">Hae K-Ruoasta: {esc(fi)} ↗</a>'
            if key in PRODUCTS:
                name,slug=PRODUCTS[key];detail+=f'<p>Tuote-esimerkki: <a href="https://www.k-ruoka.fi/kauppa/tuote/{slug}">{esc(name)}</a></p>'
            use=''.join(f'<li><a href="{recipe_link(r)}">{DAY_NAMES[r["day"]]} · {esc(r["title"])}</a>: {amount(key,q)}</li>' for r,q in uses[key])
            detail+=f'<details><summary>Reseptit ({len(uses[key])})</summary><ul>{use}</ul></details>'
            items+=f'''<div class="shop-item"><div class="shop-row"><input type="checkbox" id="shop-{key}" data-shop="{week}:{key}:{qfmt(qty)}"><label for="shop-{key}"><span><strong>{esc(cat['label'])}</strong></span><span class="quantity">{amount(key,qty)}</span></label></div><div class="shop-detail">{detail}</div></div>'''
            text_lines.append(f'[ ] {cat["label"]}: {amount(key,qty)}'+(f' — {buy}' if buy else ''))
        grid+=f'<section class="shop-group"><h2>{esc(group)}</h2>{items}</section>';text_lines.append('')
    text_lines+=['HUOMIOITA','Pakkauskoot ovat esimerkkejä, eivät vahvistettua Ruoholahden valikoimaa. Tarkista säilykkeiden valutettu paino.','Liemi mitataan valmiina, liha raakana ja riisi, pasta sekä nuudelit kuivina. Uppopaistoöljy on mukana kokonaisena eränä.','Osta tuoretuotteet lähellä käyttöpäivää tai pakasta pakkauksen ohjeen mukaan. Noudata viimeisiä käyttöpäiviä.','Saatavuus ja ainesosat voivat muuttua. Tarkista, ettei tuotteessa ole maapähkinää.','',STORE]
    shopping_text='\n'.join(text_lines)
    write(Path('lists')/f'{week}.txt',shopping_text)
    body=f'''<div class="wrap"><header class="shopping-head"><a class="crumb" href="{week}.html">← {v['name']}: ruokalista</a><p class="eyebrow" style="margin-top:22px">Viikko {v['number']} / K-Citymarket Helsinki Ruoholahti</p><h1>{v['name']}:<br>ostoslista</h1><p>{v['heads']}. Mukana ovat kaikki suunnitellut ateriat, lisukkeet ja erilliset annokset.</p><p class="small">Tarvittavat määrät on lihavoitu ja pakkausmäärät pyöristetty ylöspäin. Tarkista ensin, mitä kotona on jo. Liha on raakapainona, riisi ja pasta kuivina sekä säilykepavut ja -linssit valutettuina.</p></header><div class="note"><strong>Ostokset Ruoholahdesta</strong><p>Valitse K-Ruoassa <a href="{STORE}">K-Citymarket Helsinki Ruoholahti</a>. Tuote-esimerkit on tarkistettu K-Ruoan valikoimasta 11.9.2026, mutta Ruoholahden reaaliaikaista saatavuutta ei ole vahvistettu. Tarkista saatavuus ja pakkauksen ainesosat. ”Saattaa sisältää maapähkinää” sopii tälle perheelle.</p><p>Osta tuore liha, kala, äyriäiset ja herkästi pilaantuvat kasvikset lähellä käyttöpäivää tai pakasta pakkauksen ohjeen mukaan. Tarkista viimeiset käyttöpäivät.</p></div><div class="shop-toolbar no-print"><span class="progress" id="progress" aria-live="polite">0 / {len(totals)} merkitty</span><button class="button" data-print>Tulosta lista</button><a class="button secondary" href="lists/{week}.txt" download>Lataa tekstitiedosto</a><button class="button secondary" id="copy-list">Kopioi lista</button><button class="button secondary" id="reset-list">Poista merkinnät</button></div><p class="small no-print">Merkinnät tallentuvat tähän selaimeen. Poistaminen koskee vain tämän viikon listaa.</p><p class="status no-print" id="status" role="status"></p><div class="no-print" id="copy-fallback" hidden><label for="copy-text">Valitse ja kopioi lista:</label><textarea class="shopping-plain" id="copy-text" readonly>{esc(shopping_text)}</textarea></div><div class="shopping-grid">{grid}</div></div>'''
    write(Path(f'{week}-shopping.html'),shell(f'{v["name"]}: ostoslista',body,week))

if __name__=='__main__':
    assert len(RECIPES)==30
    assert len({r['id'] for r in RECIPES})==30
    assert all(i['key'] in FI for r in RECIPES for i in r['ingredients'])
    homepage()
    for w,v in WEEKS.items():country(w,v);shopping(w,v)
    for r in RECIPES:recipe(r)
    used={i['key'] for r in RECIPES for i in r['ingredients']}
    write(Path('assets/menu.json'),json.dumps(dict(recipes=RECIPES,ingredients={k:CAT[k] for k in sorted(used)},shopping={w:dict(sum_week(w)[0]) for w in WEEKS}),ensure_ascii=False,indent=2))
    print(f'Built 30 recipe pages, 3 country menus, 3 shopping lists and the home page.')
