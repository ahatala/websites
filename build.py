"""Generate the static GitHub Pages site: python3 build.py (no dependencies)."""
from pathlib import Path
from collections import defaultdict
from html import escape as esc
from urllib.parse import quote
from math import ceil
import json
from menu import CAT, RECIPES
from shopping import FI, PRODUCTS, PACKS, NOTES, STORE
ROOT=Path(__file__).parent
DAYS=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
ORDER={'Breakfast':0,'Lunch':1,'Lunch / snack':1,'Dinner':2,'Dessert':3}
WEEKS={
'greece':dict(name='Greece',number=1,tag='Lemon, filo & a little sunshine',desc='Fresh herbs, warm pitas and generous dishes to share. Six dinners, a Saturday off, and a Sunday worth lingering over.',heads='4 most days · 3 on Thursday · Saturday off',prep=['Check the filo thawing instructions before Tuesday. Save enough for Sunday’s feta parcels, following pack storage directions.','Thursday’s giouvetsi needs a long, gentle cook. Start early or prepare the beef ahead.','Sunday: make the two moussaka fillings side by side. Tiropita is a light lunch; doughnuts finish the day.'],activity='Let everyone fold a feta parcel, then find Greece on a map and choose music for Sunday dinner.'),
'uk':dict(name='United Kingdom',number=2,tag='Cosy classics, made for us',desc='A curry to start, a chippy night on Thursday and a cauliflower Sunday roast. Familiar comforts with room for everyone.',heads='4 Monday–Friday · 3 on the weekend',prep=['The weekend has two meat-eaters and one meat-free diner; all Saturday and Sunday recipes serve three.','Fish & chips is Thursday. Friday’s batter is split between a regular dish and a little vegetarian-sausage dish.','Sunday roast is cauliflower cheese for all three. The recipe coordinates the potatoes, Yorkshires and gravy.'],activity='Run a tiny kitchen café for breakfast: set the table, take orders and give the crumpets a name.'),
'china':dict(name='China',number=3,tag='Fold, sizzle, gather',desc='Quick stir-fries, homemade dumplings and a hot-pot finale. Mild shared bases, chilli at the table, and no peanuts in the recipes.',heads='4 every day · 3 meat + 1 meat-free when needed',prep=['Friday’s dumpling dough is made from plain flour. Fold the mushroom batch first and give it a different shape.','Saturday’s mango puddings need three hours to chill. Sunday’s sesame biscuits replace sesame balls.','For hot pot, use a shared vegetable pot and a separate beef pot. A two-pot setup on the hob works too.'],activity='Give everyone a dumpling-folding station on Friday. On Sunday, arrange the hot-pot vegetables into a colourful serving platter.')}

def qfmt(q):
    if q==int(q): return str(int(q))
    return f'{q:g}'
def amount(key,q):
    unit=CAT[key]['unit']
    value=qfmt(q)
    if unit=='tsp': value={0.25:'¼',0.5:'½',0.75:'¾',1.5:'1½'}.get(q,value)
    return value if unit=='whole' else f'{value} {unit}'
def sum_week(week):
    totals=defaultdict(float); uses=defaultdict(list)
    for r in RECIPES:
        if r['week']==week:
            for i in r['ingredients']:
                totals[i['key']]+=i['qty']; uses[i['key']].append((r,i['qty']))
    return totals,uses

def shell(title,body,week='',prefix=''):
    nav=''.join(f'<a href="{prefix}{w}.html"'+(' aria-current="page"' if week==w else '')+f'>{esc(v["name"])}</a>' for w,v in WEEKS.items())
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#203c33"><meta name="description" content="Our family food festival: three country menus, practical recipes and complete weekly K-Ruoka shopping lists."><title>{esc(title)} · Family Food Festival</title><link rel="icon" href="{prefix}assets/greece.svg" type="image/svg+xml"><link rel="stylesheet" href="{prefix}assets/style.css"><script src="{prefix}assets/app.js" defer></script></head><body class="{week}" id="top"><a class="skip" href="#main">Skip to content</a><header class="site-header"><div class="wrap header-inner"><a class="brand" href="{prefix}index.html"><span class="brand-mark" aria-hidden="true">f</span><span>FAMILY FOOD<br>FESTIVAL</span></a><nav class="nav" aria-label="Country menus">{nav}</nav></div></header><main id="main">{body}</main><footer class="footer"><div class="wrap footer-inner"><p>Made for our table, in Helsinki. Family recipe adaptations; cooking times are estimates. No peanut ingredients or salmon. Other listed allergens, including sesame, dairy and eggs, remain.</p><a href="{prefix}index.html#our-table">Our table notes</a><a href="#top">Back to top ↑</a></div></footer></body></html>'''

def write(path,content):
    target=ROOT/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(content)

def recipe_link(r,prefix=''):
    return f'{prefix}recipes/{r["id"]}.html'

def homepage():
    cards=''
    for w,v in WEEKS.items():
        dinners=sum(r['week']==w and r['kind']=='Dinner' for r in RECIPES)
        cards+=f'''<article class="country-card {w}" id="{w}"><div class="card-art"><img src="assets/{w}.svg" alt="" width="500" height="440"></div><div class="card-body"><span class="eyebrow">Week 0{v['number']} · {dinners} dinners</span><h3>{v['name']}</h3><p>{v['tag']}.<br>{v['heads']}.</p><a class="card-link" href="{w}.html">Explore the week</a></div></article>'''
    body=f'''<div class="wrap"><section class="hero"><div><span class="eyebrow">Three weeks · three countries · our family</span><h1>A little world<br>on our table.</h1><p class="intro">A family food festival, one meal at a time. Greece, the United Kingdom and China—with recipes that fit our table and shopping lists for our K-store.</p><div class="actions"><a class="button" href="#weeks">Choose a week <span aria-hidden="true">↓</span></a><a class="button secondary" href="#our-table">Meet the menu</a></div></div><div class="home-doodle"><div class="hero-art"><img src="assets/table.svg" alt="Illustration of Greek salad, a dumpling pot and a cup of tea on a checked tablecloth" width="500" height="440"><div class="stamp"><b>30</b>recipes<br>to share</div></div><p class="art-caption">Pass the plates. Try something new.</p></div></section></div><div class="ribbon"><div class="wrap"><span>20 dinners + 10 little extras</span><span>No peanut ingredients · No salmon</span><span>K-Citymarket Helsinki Ruoholahti</span></div></div><div class="wrap"><section class="section" id="weeks"><div class="section-head"><div><span class="eyebrow">The itinerary</span><h2>Where shall we eat?</h2></div><p>Each stop has a day-by-day menu, full recipes and a shopping list with every side and separate portion included.</p></div><div class="countries">{cards}</div></section><section class="section" id="our-table"><span class="eyebrow">A few things about us</span><h2>One table. Room for everyone.</h2><div class="rules"><div><span class="rule-num">01 / Ingredients</span><h3>No peanuts or salmon.</h3><p>No peanut ingredients, peanut oil, salmon or other red-fleshed fish in this plan. “May contain peanuts” is okay for this household. The fish dinner uses cod or haddock.</p></div><div><span class="rule-num">02 / Portions</span><h3>Share what we can.</h3><p>Usually three meat-eaters and one who avoids meat and poultry. Fish, eggs and dairy are okay. Shared bases plus small separate portions keep cooking manageable.</p></div><div><span class="rule-num">03 / Shopping</span><h3>Our neighbourhood shop.</h3><p><a href="{STORE}">K-Citymarket Helsinki Ruoholahti</a> is our shopping reference. Finnish search names, selected product links and practical substitutions are included.</p></div></div><p class="small" style="margin-top:16px">Quantities use standard adult-sized portions; adjust for appetites. Lists cover the meals shown, not additional breakfasts, snacks or drinks. K-Ruoka catalogue links are references, not live Ruoholahti stock checks; select the store on K-Ruoka and check the current ingredient labels.</p></section><section class="section" id="scorecard"><div class="section-head"><div><span class="eyebrow">The family verdict</span><h2>And the favourite was…</h2></div><p>Keep the judging playful. A surprising favourite counts as a very good result.</p></div><div class="score-grid"><div class="score-item"><label for="best-dish">Best dish</label><input id="best-dish" data-save="best-dish" placeholder="The one we’ll make again"></div><div class="score-item"><label for="best-dessert">Best dessert</label><input id="best-dessert" data-save="best-dessert" placeholder="A sweet winner"></div><div class="score-item"><label for="surprise">Biggest surprise</label><input id="surprise" data-save="surprise" placeholder="Didn’t expect to love it"></div><div class="score-item"><label for="winning-country">Winning country</label><select id="winning-country" data-save="winning-country"><option value="">Choose a country</option><option>Greece</option><option>United Kingdom</option><option>China</option></select></div></div><p class="small" style="margin-top:12px">Your answers are saved on this browser, not shared between devices.</p></section></div>'''
    write(Path('index.html'),shell('A little world on our table',body))

def country(week,v):
    days=''
    for day in DAYS:
        rs=sorted([r for r in RECIPES if r['week']==week and r['day']==day],key=lambda r:ORDER[r['kind']])
        if not rs:
            days+=f'<article class="day skipped"><div class="day-name">{day}<span>No cooking planned</span></div><div><h3>A day off.</h3><p class="small">No meals or shopping quantities included for Saturday.</p></div></article>';continue
        meals=''
        for r in rs:
            meals+=f'''<div class="meal"><span class="eyebrow">{r['kind']}</span><h3><a href="{recipe_link(r)}">{esc(r['title'])} ↗</a></h3><p>{esc(r['desc'])}</p><div class="meta"><span class="pill">{esc(r['split'])}</span><span>{esc(r['time'])}</span></div></div>'''
        days+=f'<article class="day"><div class="day-name">{day}<span>{rs[0]["servings"]} at the table</span></div><div>{meals}</div></article>'
    prep=''.join(f'<li>{esc(p)}</li>' for p in v['prep'])
    body=f'''<div class="wrap"><section class="hero"><div><span class="eyebrow">Week 0{v['number']} / {v['tag']}</span><h1>{v['name']}</h1><p class="intro">{v['desc']}</p><p class="pill">{v['heads']}</p><div class="actions"><a class="button" href="{week}-shopping.html">This week’s shopping ↗</a><a class="button secondary" href="#menu">See the menu ↓</a></div></div><div class="hero-art"><img src="assets/{week}.svg" alt="{esc(v['tag'])}: illustrated food" width="500" height="440"><div class="stamp"><b>0{v['number']}</b>family<br>food festival</div></div></section><nav class="subnav" aria-label="Week sections"><a href="#menu">The menu</a><a href="{week}-shopping.html">Shopping list</a><a href="#kitchen-notes">Kitchen notes</a></nav><section class="section" id="menu"><div class="section-head"><div><span class="eyebrow">What’s cooking</span><h2>A week at our table.</h2></div><p>Open any dish for quantities, method and the plan for separate portions.</p></div><div class="week-layout"><div class="days">{days}</div><aside class="aside" id="kitchen-notes"><div><h3>A little head start</h3><ul>{prep}</ul></div><div><h3>Make it a festival</h3><p>{v['activity']}</p><a class="button" href="{week}-shopping.html">Get the shopping list</a><p class="small" style="margin-top:15px">Includes all meals shown, pantry ingredients and the meat-free portions.</p></div></aside></div></section></div>'''
    write(Path(f'{week}.html'),shell(v['name'],body,week))

def recipe(r):
    week=r['week'];v=WEEKS[week]
    items=''.join(f'<li><span>{esc(CAT[i["key"]]["label"])}</span><span class="quantity">{amount(i["key"],i["qty"])}</span></li>' for i in r['ingredients'])
    steps=''.join(f'<li>{esc(s)}</li>' for s in r['steps'])
    note=f'<div class="note"><strong>Kitchen note</strong><p>{esc(r["note"])}</p></div>' if r['note'] else ''
    source=''
    if r['id']=='hot-pot': source='<p class="small">More setup ideas: <a href="https://thewoksoflife.com/chinese-hot-pot-at-home/">The Woks of Life’s hot-pot guide</a>. Use our peanut-free ingredient list and separate-pot plan above.</p>'
    body=f'''<div class="wrap"><header class="recipe-top"><a class="crumb" href="../{week}.html#menu">← Week {v['number']} · {v['name']}</a><p class="eyebrow" style="margin-top:22px">{r['day']} / {r['kind']}</p><h1>{esc(r['title'])}</h1><p class="desc">{esc(r['desc'])}</p><div class="meta"><span class="pill">Serves {r['servings']}</span><span class="pill">{esc(r['split'])}</span><span class="pill">{esc(r['time'])}</span></div><div class="actions"><button class="button" data-print>Print recipe</button><a class="button secondary" href="../{week}-shopping.html">Weekly shopping list</a></div></header><div class="recipe-layout"><section class="ingredients"><h2>What you’ll need</h2><p class="small">Total for all {r['servings']} portions, including sides and any separate version. Water is listed in the method.</p><ul>{items}</ul></section><section class="method"><h2>Let’s cook.</h2><p class="small">Oven temperatures are for fan ovens. For conventional ovens, use about 20°C higher.</p><ol class="steps">{steps}</ol>{note}{source}<p class="small" style="margin-top:20px">Cooking times vary with equipment and ingredient size. <a href="https://www.gov.uk/food-hygiene-businesses/cooking">Cooking guidance</a>: where a core temperature is specified, check with a clean food thermometer.</p></section></div><nav class="recipe-links" aria-label="Recipe navigation"><a href="../{week}.html#menu">← Back to the week</a><a href="../{week}-shopping.html">Shopping for {v['name']} →</a></nav></div>'''
    write(Path('recipes')/f'{r["id"]}.html',shell(r['title'],body,week,'../'))

def buying(key,qty):
    if key in PACKS:
        size=PACKS[key];n=ceil(round(qty/size,8))
        unit_amount=f'{size} eggs' if key=='egg' else amount(key,size)
        return f'Plan for {n} pack'+('s' if n>1 else '')+f' of {unit_amount} (before checking your pantry).'
    if key=='stock':return f'Enough cubes or concentrate to make {qfmt(qty/1000)} litres.'
    if key=='lemon':return f'Buy at least {ceil(qty)} lemons.'
    if key=='garlic':return f'Buy at least {ceil(qty)} cloves; roughly {ceil(qty/8)} bulbs.'
    return ''

def shopping(week,v):
    totals,uses=sum_week(week);groups=defaultdict(list)
    for key in sorted(totals,key=lambda k:CAT[k]['label']):groups[CAT[key]['group']].append(key)
    text_lines=[f'FAMILY FOOD FESTIVAL — WEEK {v["number"]}: {v["name"].upper()}',v['heads'],'K-Citymarket Helsinki Ruoholahti','All scheduled meals, sides and separate portions. Exact quantities needed; subtract what you already have.','No peanut ingredients or salmon. May-contain-peanuts products are okay.','']
    grid=''
    for group in dict.fromkeys(CAT[k]['group'] for k in CAT):
        if group not in groups:continue
        items='';text_lines.append(group.upper())
        for key in groups[group]:
            qty=totals[key];cat=CAT[key];fi=FI[key];search=f'https://www.k-ruoka.fi/kauppa/tuotehaku?haku={quote(fi)}'
            buy=buying(key,qty);detail=f'<p>{esc(buy)}</p>' if buy else ''
            if key in NOTES:detail+=f'<p>{esc(NOTES[key])}</p>'
            detail+=f'<a href="{search}">Find “{esc(fi)}” at K-Ruoka ↗</a>'
            if key in PRODUCTS:
                name,slug=PRODUCTS[key];detail+=f'<p>Catalogue example: <a href="https://www.k-ruoka.fi/kauppa/tuote/{slug}">{esc(name)}</a></p>'
            use=''.join(f'<li><a href="{recipe_link(r)}">{r["day"]} · {esc(r["title"])}</a>: {amount(key,q)}</li>' for r,q in uses[key])
            detail+=f'<details><summary>Used in {len(uses[key])} recipe'+('s' if len(uses[key])>1 else '')+f'</summary><ul>{use}</ul></details>'
            items+=f'''<div class="shop-item"><div class="shop-row"><input type="checkbox" id="shop-{key}" data-shop="{week}:{key}:{qfmt(qty)}"><label for="shop-{key}"><span><strong>{esc(cat['label'])}</strong><span class="finnish">{esc(fi)}</span></span><span class="quantity">{amount(key,qty)}</span></label></div><div class="shop-detail">{detail}</div></div>'''
            text_lines.append(f'[ ] {cat["label"]} / {fi}: {amount(key,qty)}'+(f' — {buy}' if buy else ''))
        grid+=f'<section class="shop-group"><h2>{esc(group)}</h2>{items}</section>';text_lines.append('')
    text_lines+=['NOTES','Suggested pack sizes are planning aids, not confirmed Ruoholahti stock. For drained tins check the label.','Stock is measured prepared, meat is raw, rice/pasta/noodles are dry. Frying oil is included as a full batch.','Shop fresh items near the day of use, or freeze according to the pack; use-by dates determine storage.','Product labels and availability can change. Check the current labels for peanut ingredients.','',STORE]
    shopping_text='\n'.join(text_lines)
    write(Path('lists')/f'{week}.txt',shopping_text)
    body=f'''<div class="wrap"><header class="shopping-head"><a class="crumb" href="{week}.html">← {v['name']} menu</a><p class="eyebrow" style="margin-top:22px">Week 0{v['number']} / K-Citymarket Helsinki Ruoholahti</p><h1>{v['name']}:<br>the shopping list.</h1><p>{v['heads']}. Every scheduled meal, side and separate portion is included.</p><p class="small">Exact amounts needed are shown in bold. Suggested packs are rounded up; subtract pantry supplies first. Meat is raw, rice and pasta are dry, and tinned beans and lentils are drained. Water is not a shopping item.</p></header><div class="note"><strong>Shopping at Ruoholahti</strong><p>Start with <a href="{STORE}">K-Citymarket Helsinki Ruoholahti</a> and select it on K-Ruoka. Ingredient searches and the specialist product examples across the site use the K-Ruoka catalogue checked on 11 September 2026. Live Ruoholahti availability has not been verified; check the selected store and current package labels. No peanut ingredients; “may contain peanuts” is okay for this household.</p><p>Buy fresh meat, seafood and delicate produce near their cooking days, or freeze according to the pack. Check use-by dates rather than assuming everything will keep for a week.</p></div><div class="shop-toolbar no-print"><span class="progress" id="progress" aria-live="polite">0 of {len(totals)} checked</span><button class="button" data-print>Print list</button><a class="button secondary" href="lists/{week}.txt" download>Download .txt</a><button class="button secondary" id="copy-list">Copy list</button><button class="button secondary" id="reset-list">Clear ticks</button></div><p class="small no-print">Ticks stay on this browser. Clear ticks affects this week only.</p><p class="status no-print" id="status" role="status"></p><div class="no-print" id="copy-fallback" hidden><label for="copy-text">Select and copy your list:</label><textarea class="shopping-plain" id="copy-text" readonly>{esc(shopping_text)}</textarea></div><div class="shopping-grid">{grid}</div></div>'''
    write(Path(f'{week}-shopping.html'),shell(f'{v["name"]} shopping list',body,week))

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
