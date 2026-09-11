"""Finnish editorial text. Ingredient quantities and recipe IDs stay unchanged."""
DAYS={'Monday':'Maanantai','Tuesday':'Tiistai','Wednesday':'Keskiviikko','Thursday':'Torstai','Friday':'Perjantai','Saturday':'Lauantai','Sunday':'Sunnuntai'}
KINDS={'Dinner':'Päivällinen','Breakfast':'Aamiainen','Lunch':'Lounas','Lunch / snack':'Lounas / välipala','Dessert':'Jälkiruoka'}
LABELS=dict(potato='Peruna',onion='Sipuli',redonion='Punasipuli',tomato='Tomaatti',cucumber='Kurkku',carrot='Porkkana',celery='Varsiselleri',spinach='Pakastepinaatti',aubergine='Munakoiso',mushroom='Herkkusienet',leek='Purjo',salad='Salaatinlehdet',pepper='Paprika',cabbage='Kiinankaali',pakchoi='Paksoi',cauliflower='Kukkakaali (puhdistettuna)',ginger='Tuore inkivääri',spring='Kevätsipuli',apple='Omena',mango='Mango (hedelmäliha, tuore tai pakaste)',lemon='Sitruuna',garlic='Valkosipulinkynnet',dill='Tuore tilli',parsley='Tuore persilja',chicken='Broilerin luuton liha',beef='Naudan pataliha',mince='Naudan jauheliha',pork='Luuton porsaan kassler',porkmince='Porsaan jauheliha',hotbeef='Naudanliha ohuina viipaleina',prawn='Raa’at kuoritut katkaravut',cod='Ruodoton turska- tai koljafilee',tofu='Kiinteä tofu',softtofu='Pehmeä tofu',halloumi='Halloumi',paneer='Paneerjuusto',sausage='Porsaan raakamakkara',vegsausage='Kasvismakkara',bacon='Pekoni',feta='Feta',yogurt='Kreikkalainen jogurtti',butter='Voi',cheddar='Cheddar',hardcheese='Cheddar',milk='Maito',cream='Kuohukerma',egg='Kananmunat',bread='Leipä',filo='Filotaikina',pita='Pitaleivät',naan='Naanleivät',whitebean='Valkoiset säilykepavut',lentil='Vihreät tai ruskeat säilykelinssit',tintomato='Tomaattimurska',puree='Tomaattipyree',peas='Pakasteherneet',bakedbeans='Valkoiset pavut tomaattikastikkeessa',icecream='Vaniljajäätelö',coconut='Kookosmaito',custard='Valmis vaniljakastike',orzo='Orzo-jyväpasta (kuiva)',rice='Jasmiiniriisi (kuiva)',basmati='Basmatiriisi (kuiva)',noodles='Vehnänuudelit (kuiva)',flour='Vehnäjauho',cornflour='Maissitärkkelys',sugar='Sokeri',brownsugar='Fariinisokeri',date='Kivettömät taatelit',sesame='Seesaminsiemenet',baking='Leivinjauhe',bicarb='Ruokasooda',yeast='Kuivahiiva',vanilla='Vaniljauute',agar='Agar-agar-jauhe',olive='Oliiviöljy',oil='Rypsiöljy (myös uppopaistoon)',soy='Soijakastike',vinegar='Riisiviinietikka',sesameoil='Paahdettu seesamiöljy',malt='Mallasetikka',honey='Hunaja',jam='Hillo',mustard='Dijon-sinappi',mayo='Majoneesi',caper='Kaprikset',gherkin='Maustekurkut',hoisin='Hoisinkastike (ei maapähkinää)',chilli='Chilirouhe (tarjolle erikseen)',beanpaste='Vegaaninen misotahna',stock='Kasvisliemi (valmiiksi laimennettu)',salt='Suola',blackpepper='Mustapippuri',oregano='Kuivattu oregano',cinnamon='Jauhettu kaneli',nutmeg='Jauhettu muskottipähkinä',cumin='Juustokumina',coriander='Jauhettu korianteri',garam='Garam masala',paprika='Paprikajauhe',turmeric='Kurkuma',thyme='Kuivattu timjami',bay='Laakerinlehdet')
GROUPS={'Vegetables & fruit':'Kasvikset ja hedelmät','Meat, fish & alternatives':'Liha, kala ja kasviproteiinit','Dairy & eggs':'Maitotuotteet ja kananmunat','Bakery & chilled':'Leivät ja taikinat','Tins & freezer':'Säilykkeet ja pakasteet','Rice, flour & baking':'Riisi, jauhot ja leivonta','Oils, sauces & pantry':'Öljyt, kastikkeet ja muut kuiva-aineet','Spices & seasoning':'Mausteet'}
TEXT={}
def t(id,title,desc,time,split,steps,note=''):
    TEXT[id]=dict(title=title,desc=desc,time=time,split=split,steps=steps,note=note)
t('souvlaki','Kana- ja halloumisouvlakit','Pitaleipiä, tsatsikia ja salaattikasviksia kana- tai halloumivartaiden kanssa.','40 min + marinointi 20 min','3 kana-annosta + 1 halloumiannos',[
'Kuutioi broileri. Sekoita oliiviöljy, puolet sitruunamehusta, yksi murskattu valkosipulinkynsi, oregano, puolet suolasta ja mustapippuri. Ota neljännes marinadista puhtaaseen kulhoon halloumia varten. Sekoita broileri loppuun marinadiin ja anna maustua jääkaapissa 20 minuuttia.',
'Raasta 150 g kurkkua ja purista neste pois. Sekoita raaste jogurttiin. Lisää loput valkosipulista, sitruunamehusta ja suolasta. Viipaloi loppu kurkku, tomaatit ja punasipuli.',
'Pujota broileri vartaisiin. Liota puiset varrastikut ensin. Grillaa tai paista keskilämmöllä tai hieman kuumemmalla pannulla 10–14 minuuttia välillä kääntäen. Broilerin sisälämpötilan tulee olla vähintään 75 °C 30 sekunnin ajan.',
'Leikkaa halloumi paksuiksi paloiksi ja sekoita omaan marinadiinsa. Paista erillisellä pannulla 2–3 minuuttia kummaltakin puolelta. Lämmitä pitaleivät ja täytä ne vartaiden sisällöllä, tsatsikilla ja kasviksilla.' ])
t('spanakopita','Spanakopita ja kreikkalainen salaatti','Pinaatti-fetapiirakka filotaikinasta.','65 min','Kasvisruoka kaikille',[
'Lämmitä kiertoilmauuni 180 asteeseen. Sulata pinaatti ja purista se mahdollisimman kuivaksi. Hienonna sipuli ja kuullota sitä 15 ml:ssa öljyä 8 minuuttia. Anna jäähtyä hieman.',
'Sekoita pinaatti, sipuli, 200 g murennettua fetaa, kananmunat, hienonnettu tilli, mustapippuri ja puolet suolasta. Varaa 30 ml öljyä vuoan ja taikinalevyjen voiteluun. Voitele noin 20 × 25 cm:n vuoka. Lado puolet filolevyistä vuokaan ja sivele kerrosten väliin hieman öljyä. Pidä käyttämättömät levyt kostean pyyhkeen alla.',
'Levitä täyte vuokaan ja peitä lopuilla filolevyillä. Voitele varatulla öljyllä, taita reunat sisään ja leikkaa pintaan kevyesti neljän annoksen rajat. Paista 35–40 minuuttia, kunnes pinta on rapea ja täyte hyytynyt.',
'Pilko tomaatit, kurkku ja punasipuli. Mausta jäljellä olevalla 15 ml:lla öljyä, sitruunamehulla, oreganolla ja lopulla suolalla. Lisää loput 100 g fetaa. Tarjoa piirakan kanssa.' ])
t('fasolada','Fasolada-papukeitto','Valkopapu-kasviskeittoa, leipää ja fetaa.','45 min','Kasvisruoka kaikille',[
'Kuutioi sipuli, porkkanat ja selleri. Kuullota niitä oliiviöljyssä suuressa kattilassa 10 minuuttia. Lisää hienonnettu valkosipuli ja jatka minuutti.',
'Lisää tomaattimurska, valutetut pavut, kasvisliemi, oregano ja laakerinlehti. Keitä hiljalleen 25 minuuttia, kunnes porkkanat ovat pehmeitä.',
'Murskaa kauhallinen papuja kattilan reunaa vasten, jotta keitto sakenee hieman. Poista laakerinlehti. Mausta suolalla ja mustapippurilla. Vähennä suolaa, jos liemi on jo suolainen.',
'Lämmitä leipä ja tarjoa keiton sekä erikseen murennetun fetan kanssa.' ],'720 g valutettuja papuja vastaa noin kolmea 400 g:n säilyketölkkiä. Tarkista valutettu paino pakkauksesta.')
t('giouvetsi','Naudanliha-giouvetsi','Pitkään haudutettua naudanlihaa ja orzoa tomaattikastikkeessa.','2 h 30 min','3 liha-annosta · kasvissyöjä poissa',[
'Lämmitä kiertoilmauuni 160 asteeseen. Leikkaa naudanliha noin 3 cm:n kuutioiksi. Ruskista öljyssä uuninkestävässä padassa muutamassa erässä ja siirrä sivuun. Kuullota hienonnettua sipulia samassa padassa 8 minuuttia.',
'Lisää hienonnettu valkosipuli ja tomaattipyree. Sekoita minuutti. Palauta liha pataan ja lisää tomaattimurska, 400 ml lientä, kaneli, laakerinlehti, suola ja mustapippuri. Peitä ja hauduta uunissa 1½–2 tuntia, kunnes liha on haarukalla kokeiltaessa mureaa.',
'Nosta uunin lämpö 180 asteeseen. Poista laakerinlehti. Sekoita joukkoon kuiva orzo ja loput 300 ml kuumaa lientä. Paista ilman kantta 20–25 minuuttia ja sekoita puolivälissä. Lisää tilkka kuumaa vettä, jos pasta kuivuu ennen kypsymistä.',
'Anna vetäytyä 10 minuuttia. Orzo imee vielä kastiketta. Tarjoa juustoraasteen kanssa.' ])
t('saganaki','Katkarapusaganaki','Katkarapuja tomaatti-fetakastikkeessa, leipää ja kreikkalaista salaattia.','35 min','Sama ruoka kaikille',[
'Lämmitä kiertoilmauuni 200 asteeseen. Kuullota hienonnettua sipulia 25 ml:ssa öljyä uuninkestävällä pannulla 8 minuuttia. Lisää hienonnettu valkosipuli ja oregano minuutiksi. Lisää tomaattimurska, suola ja mustapippuri. Hauduta 12–15 minuuttia, kunnes kastike sakenee.',
'Kuivaa sulatetut, kuoritut katkaravut. Sekoita ne kastikkeeseen ja murenna päälle 150 g fetaa. Paista uunissa 8–12 minuuttia, kunnes ravut ovat kauttaaltaan läpikuultamattomia ja kypsiä.',
'Pilko tuoreet tomaatit, kurkku ja punasipuli. Mausta lopulla 15 ml:lla öljyä ja puolella sitruunamehusta. Lisää loput 50 g fetaa.',
'Ripottele katkarapujen päälle hienonnettua persiljaa. Tarjoa leivän, salaatin ja jäljelle jääneestä sitruunasta leikattujen lohkojen kanssa.' ])
t('moussaka','Moussaka: liha- ja kasvisversio','Kolme annosta naudanlihalla ja yksi linsseillä ja sienillä. Kasvikset ja valkokastike valmistetaan yhdessä.','1 h 50 min','3 liha-annosta + 1 kasvisannos',[
'Lämmitä kiertoilmauuni 200 asteeseen. Viipaloi perunat ja munakoisot noin 5 mm:n paksuisiksi. Sekoita joukkoon 45 ml öljyä ja puolet suolasta. Paahda leivinpaperilla vuoratuilla pelleillä 25–30 minuuttia. Käännä kerran ja kypsennä pehmeiksi.',
'Kuullota hienonnettua sipulia lopussa 15 ml:ssa öljyä 8 minuuttia. Lisää valkosipuli ja tomaattipyree minuutiksi. Lisää tomaattimurska, kaneli, oregano, loput suolasta ja mustapippuri. Hauduta 15 minuuttia. Jaa kastike kahteen kulhoon: kolme neljäsosaa lihaversioon ja yksi neljäsosa kasvisversioon.',
'Ruskista jauhelihaa suurella pannulla 8–10 minuuttia ja murenna se lastalla. Lisää suurempi kastikeannos ja hauduta 10 minuuttia. Paista hienonnettuja sieniä erillisellä pienellä pannulla ilman öljyä, kunnes neste haihtuu. Lisää valutetut linssit ja pienempi kastikeannos. Hauduta 5 minuuttia.',
'Sulata voi kattilassa, sekoita joukkoon jauhot ja kypsennä minuutti. Lisää maito vähitellen vispaten. Keitä hiljalleen koko ajan sekoittaen, kunnes kastike sakenee. Lisää muskottipähkinä ja puolet juustosta.',
'Laske uunin lämpö 180 asteeseen. Varaa lihaversiolle noin 20 × 20 cm:n vuoka ja kasvisversiolle noin 12 × 15 cm:n vuoka. Jaa perunat, munakoisot ja valkokastike vuokiin suhteessa 3:1. Lado pohjalle perunat, sitten munakoiso ja täyte. Levitä päälle valkokastike ja loput juustosta.',
'Paista 35–40 minuuttia, kunnes pinta on kullanruskea ja ruoka kuplii sekä on kauttaaltaan kuumaa. Lihatäytteen sisälämpötilan tulee olla vähintään 75 °C 30 sekunnin ajan. Anna vetäytyä 15 minuuttia ennen tarjoilua.' ])
t('tiropita','Tiropita-fetapiiraat','Kahdeksan pientä filotaikinapiirasta neljälle.','40 min','Kasvisruoka kaikille',[
'Lämmitä kiertoilmauuni 180 asteeseen. Murenna feta ja sekoita jogurtin, kananmunan ja mustapippurin kanssa. Sulata voi.',
'Leikkaa filotaikina noin 10 cm leveiksi suikaleiksi. Käytä kuhunkin kahdeksaan piiraaseen kaksi kerrosta ja sivele väliin hieman voita. Pidä loput taikinasta kostean pyyhkeen alla.',
'Laita suikaleen päähän kahdeksasosa täytteestä. Taita yksi kulma täytteen yli kolmioksi ja jatka taittelua suikaleen loppuun. Sulje täyte huolellisesti taikinan sisään.',
'Sivele loppu voi piiraiden päälle. Paista leivinpaperin päällä 20–25 minuuttia, kunnes pinta on kullanruskea ja täyte hyytynyt. Anna jäähtyä 5 minuuttia.' ])
t('loukoumades','Loukoumades-hunajamunkit','Pieni erä hunajalla ja kanelilla maustettuja munkkeja.','35 min + kohotus 1 h','Noin 16 pientä munkkia neljälle',[
'Sekoita jauhot, hiiva, sokeri ja suola. Vatkaa joukkoon 200 ml kädenlämpöistä vettä paksuksi, tahmeaksi taikinaksi. Peitä ja kohota lämpimässä noin tunti, kunnes taikina kuplii ja on kaksinkertaistunut.',
'Lämmitä hunaja ja 20 ml vettä pienessä kattilassa. Siirrä sivuun. Kuumenna rypsiöljy 175 asteeseen syvässä, paksupohjaisessa kattilassa. Öljyä saa olla enintään kolmannes kattilan tilavuudesta. Käytä lämpömittaria ja pidä lapset poissa paistoalueelta.',
'Laske taikinaa öljyyn pieninä nokareina kahden kostean teelusikan avulla. Paista erissä 3–4 minuuttia välillä käännellen, kunnes munkit ovat kullanruskeita ja sisältä kypsiä. Pidä öljy noin 175-asteisena. Valuta talouspaperilla.',
'Kääntele munkit hunajaliemessä, ripottele päälle kanelia ja tarjoa lämpiminä.' ],'Ostoslistassa on mukana koko paistoöljyerä, ei vain ruokaan imeytyvä määrä. Jos 750 ml ei riitä sopivaan paistosyvyyteen, käytä kapeampaa tarkoitukseen sopivaa kattilaa. Älä täytä kattilaa liian täyteen.')
t('tikka','Kana- ja paneer-tikka masala','Yhteinen mieto kastike, erikseen kypsennetyt proteiinit, basmatiriisiä ja naanleipää.','45 min','3 kana-annosta + 1 paneerannos',[
'Keitä riisi pakkauksen ohjeen mukaan. Hienonna sipuli ja kuullota 15 ml:ssa öljyä 8 minuuttia. Lisää raastettu inkivääri, murskattu valkosipuli ja kaikki mausteet suolaa lukuun ottamatta. Sekoita minuutti.',
'Lisää tomaattimurska ja suola. Hauduta 15 minuuttia. Sekoita kerma ja jogurtti joukkoon miedolla lämmöllä. Jaa kastike kahteen pannuun: kolme neljäsosaa broilerille ja yksi neljäsosa paneerille.',
'Kuutioi broileri. Ruskista 10 ml:ssa öljyä 5 minuuttia, lisää omaan kastikkeeseensa ja hauduta 12–15 minuuttia. Broilerin tulee olla läpikypsää ja sisälämpötilan vähintään 75 °C 30 sekunnin ajan.',
'Kuutioi paneer ja ruskista erillisellä pannulla lopussa 5 ml:ssa öljyä 5 minuuttia. Lisää omaan kastikkeeseensa ja hauduta 5 minuuttia. Lämmitä naanleivät pakkauksen ohjeen mukaan. Tarjoa riisin kanssa.' ],'Jos paneeria ei löydy, käytä sama grammamäärä kiinteää tofua.')
t('cottage','Linssi-sienipaistos perunamuusilla','Linssi-sienitäyte perunamuusikerroksen alla.','65 min','Kasvisruoka kaikille',[
'Lämmitä kiertoilmauuni 190 asteeseen. Kuori ja pilko perunat. Keitä 15–20 minuuttia pehmeiksi, valuta ja soseuta maidon, voin ja puolen suolamäärän kanssa.',
'Kuutioi sipulit ja porkkanat. Kuullota oliiviöljyssä 8 minuuttia. Lisää pilkotut sienet ja paista 8 minuuttia, kunnes neste haihtuu. Lisää valkosipuli, timjami ja tomaattipyree, sitten jauhot. Sekoita minuutti.',
'Lisää liemi, valutetut linssit, soijakastike, mustapippuri ja loput suolasta. Hauduta 10 minuuttia, kunnes täyte sakenee. Kaada noin 20 × 25 cm:n uunivuokaan.',
'Levitä muusi täytteen päälle, vedä pintaan uria haarukalla ja ripottele päälle cheddar. Paista 25 minuuttia, kunnes täyte kuplii ja pinta on kullanruskea.' ])
t('leek-soup','Purjo-perunakeitto ja juustoleivät','Sosekeittoa ja pannulla paistettuja cheddarvoileipiä.','40 min','Kasvisruoka kaikille',[
'Pese purjot huolellisesti ja viipaloi. Hienonna sipuli. Kuullota molempia 25 g:ssa voita 10 minuuttia ruskistamatta.',
'Lisää kuoritut, kuutioidut perunat ja liemi. Keitä hiljalleen 20 minuuttia, kunnes perunat ovat hyvin pehmeitä. Soseuta sileäksi. Lisää maito, suola ja mustapippuri ja lämmitä varovasti.',
'Tee leivästä ja cheddarista neljä kerrosvoileipää. Voitele ulkopinnat ohuelti jäljellä olevalla 25 g:lla voita. Paista melko miedolla lämmöllä 3–4 minuuttia kummaltakin puolelta, kunnes pinta on kullanruskea ja juusto sulanut.',
'Leikkaa voileivät suikaleiksi tai kolmioiksi ja tarjoa keiton kanssa.' ])
t('fish-chips','Fish & chips','Taikinoitua vaaleaa kalaa, uuniranskalaisia, hernesosetta ja tartarkastiketta.','55 min','Sama ruoka kaikille · turskaa tai koljaa',[
'Lämmitä kiertoilmauuni 210 asteeseen. Leikkaa perunat paksuiksi tikuiksi. Keitä 5 minuuttia, valuta ja anna höyryn haihtua. Sekoita joukkoon 30 ml öljyä ja puolet suolasta. Paahda 35–40 minuuttia ja käännä puolivälissä.',
'Sekoita majoneesiin hienonnetut kaprikset, maustekurkut ja puolet sitruunamehusta. Keitä herneet pakkauksen ohjeen mukaan ja valuta. Soseuta karkeasti voin, mustapippurin ja 30 ml:n kuumaa vettä kanssa.',
'Kuivaa kala ja tarkista ruodot. Jauhota fileet 30 g:lla vehnäjauhoa. Sekoita loput 150 g jauhoa, maissitärkkelys, leivinjauhe ja loppu suola. Vatkaa joukkoon 230 ml hyvin kylmää vettä juuri ennen paistamista.',
'Kuumenna loppu öljy syvässä, paksupohjaisessa kattilassa 175 asteeseen. Täytä kattilasta enintään kolmannes. Kasta kalat taikinaan ja laske varovasti öljyyn. Paista erissä 6–9 minuuttia paksuuden mukaan, kunnes pinta on rapea ja kala kypsää. Tarkista paksuimmasta kohdasta vähintään 75 °C:n sisälämpötila 30 sekunnin ajan.',
'Valuta talouspaperilla. Tarjoa heti perunoiden, hernesoseen, tartarkastikkeen, mallasetikan ja loppusitruunasta leikattujen lohkojen kanssa.' ],'Käytä öljyn lämpötilan mittaamiseen lämpömittaria. Ostoslista sisältää koko paistoöljyerän. Jos haluat valmistaa kaiken uunissa, voit ostaa maapähkinättömiä leivitettyjä turska- tai koljafileitä. Korvaa tällöin kala ja taikinan ainekset ostoslistalla ja noudata pakkauksen ohjetta.')
t('toad','Toad in the hole eli makkarapannukakku','Makkaroita uunipannukakussa, sipulikastiketta, herneitä ja porkkanoita.','55 min','3 liha-annosta + 1 kasvismakkara-annos',[
'Lämmitä kiertoilmauuni 210 asteeseen. Vatkaa 140 g jauhoa, kananmunat, maito ja suola tasaiseksi taikinaksi. Anna levätä uunin lämmetessä. Laita porsaanmakkarat ja 20 ml öljyä keskikokoiseen vuokaan. Laita kasvismakkarat ja 10 ml öljyä erilliseen pieneen vuokaan. Paista 15 minuuttia.',
'Kaada kolme neljäsosaa taikinasta porsaanmakkaroiden ympärille ja loput kasvismakkaroiden ympärille. Paista vielä 25–30 minuuttia avaamatta luukkua. Pinnan tulee olla kohonnut ja kullanruskea, ja porsaanmakkaroiden sisälämpötilan vähintään 75 °C 30 sekunnin ajan.',
'Viipaloi kastiketta varten sipulit ja kuullota voissa sekä lopussa 5 ml:ssa öljyä 15 minuuttia. Lisää loput 20 g jauhoa ja sitten vähitellen liemi, soijakastike, timjami ja mustapippuri. Hauduta 10 minuuttia.',
'Kuori ja viipaloi porkkanat. Höyrytä tai keitä 8–10 minuuttia. Valmista herneet pakkauksen ohjeen mukaan. Tarjoa molemmat makkarapannukakut yhteisen kasvispohjaisen sipulikastikkeen ja kasvisten kanssa.' ])
t('rarebit','Welsh rarebit ja tomaattikeitto','Sinappisia cheddarleipiä, pieni annos tomaattikeittoa ja vihersalaattia.','30 min','Kasvisruoka kaikille kolmelle',[
'Hienonna sipuli ja kuullota 10 ml:ssa oliiviöljyä 6 minuuttia. Lisää tomaattimurska, liemi ja suola. Hauduta 15 minuuttia ja soseuta keitoksi.',
'Sulata voi pienessä kattilassa. Lisää jauhot ja sekoita minuutti. Vatkaa maito vähitellen joukkoon paksuksi tahnaksi. Ota pois lämmöltä ja sekoita joukkoon juustoraaste, sinappi, soijakastike, mallasetikka ja mustapippuri.',
'Paahda kuusi leipäviipaletta kevyesti molemmin puolin. Levitä juustoseos päälle ja kuorruta pellillä grillivastuksen alla 3–5 minuuttia, kunnes pinta kuplii ja ruskistuu. Tarkkaile leipiä koko ajan.',
'Mausta salaatinlehdet lopulla 5 ml:lla oliiviöljyä ja sitruunamehulla. Tarjoa leipien ja pienten keittoannosten kanssa.' ],'Soijakastike ja mallasetikka korvaavat tässä Worcestershire-kastikkeen.')
t('cauliflower','Kukkakaaligratiini sunnuntain lisukkeilla','Kukkakaalia juustokastikkeessa, paahdettuja perunoita, Yorkshire-vanukkaita, kasviksia ja sipulikastiketta.','80 min','Kasvisruoka kaikille kolmelle',[
'Lämmitä kiertoilmauuni 200 asteeseen. Vatkaa 75 g jauhoa, kananmunat, 150 ml maitoa ja ¼ tl suolaa taikinaksi. Anna levätä. Kuori ja pilko perunat. Keitä 8 minuuttia, valuta ja ravistele pinnat karheiksi. Sekoita 30 ml öljyä joukkoon ja paahda 50–60 minuuttia. Käännä puolivälissä.',
'Leikkaa kukkakaali kukinnoiksi. Höyrytä 6–8 minuuttia juuri ja juuri kypsäksi ja valuta huolellisesti. Sulata 40 g voita, lisää 40 g jauhoa ja sekoita minuutti. Lisää loput 400 ml maitoa vähitellen vispaten. Keitä hiljalleen paksuksi. Lisää sinappi, 140 g cheddaria ja puolet mustapippurista.',
'Laita kukkakaali noin 20 cm:n uunivuokaan. Kaada juustokastike päälle ja lisää loppu juusto. Paista 25 minuuttia kullanruskeaksi. Nosta pois ja peitä löyhästi, jotta gratiini pysyy lämpimänä Yorkshire-vanukkaiden paistuessa. Perunat voivat jäädä uuniin rapeutumaan.',
'Kuullota kastiketta varten viipaloituja sipuleita lopussa 20 g:ssa voita 15 minuuttia. Sekoita joukkoon loput 30 g jauhoa, sitten liemi, soijakastike, timjami sekä loput mustapippurista ja suolasta. Hauduta 10 minuuttia.',
'Nosta uunin lämpö 210 asteeseen. Jaa loput 25 ml öljyä metallisen muffinivuoan kuuteen koloon ja kuumenna vuokaa 5 minuuttia. Kaada taikina tasaisesti kuumiin koloihin. Paista 20–25 minuuttia avaamatta luukkua, kunnes vanukkaat ovat kohonneet ja kullanruskeita.',
'Höyrytä viipaloituja porkkanoita 8–10 minuuttia ja valmista herneet pakkauksen ohjeen mukaan. Tarjoa kaikki yhdessä. Yorkshire-vanukkaita tulee kaksi kullekin.' ])
t('full-english','Englantilainen aamiainen','Kananmunia, papuja, kasviksia ja paahtoleipää. Kahdelle lihaa, yhdelle kasvismakkaraa.','30 min','2 liha-aamiaista + 1 kasvisaamiainen',[
'Lämmitä kiertoilmauuni 190 asteeseen. Laita porsaanmakkarat ja pekoni yhdelle pellille ja kasvismakkarat erilliselle pienelle pellille. Kypsennä pakkausten ohjeiden mukaan. Raakamakkaroihin kuluu yleensä 20–25 minuuttia; tarkista vähintään 75 °C:n sisälämpötila 30 sekunnin ajan.',
'Puolita tomaatit ja viipaloi sienet. Paista erillisellä pannulla 10 ml:ssa öljyä 8–10 minuuttia ja mausta mustapippurilla. Kuumenna pavut kattilassa.',
'Paista kananmunat lopussa 5 ml:ssa öljyä haluttuun kypsyyteen. Paahda ja voitele leivät.',
'Jaa kananmunat, pavut, sienet, tomaatit ja leivät kolmelle lautaselle. Lisää kahdelle porsaanmakkaraa ja pekonia, yhdelle kasvismakkaraa.' ])
t('toffee','Taatelivanukas toffeekastikkeella','Pieni sticky toffee pudding kolmelle, lisänä vaniljajäätelöä.','50 min','Kolme annosta',[
'Lämmitä kiertoilmauuni 170 asteeseen. Hienonna taatelit ja kaada päälle 120 ml kiehuvaa vettä. Sekoita ruokasooda joukkoon ja anna seistä 10 minuuttia. Murskaa haarukalla.',
'Vatkaa 35 g pehmeää voita ja 40 g fariinisokeria. Vatkaa joukkoon kananmuna ja vaniljauute. Kääntele joukkoon jauhot, leivinjauhe ja taateliseos.',
'Vuoraa pieni, noin 15 cm:n uunivuoka leivinpaperilla ja kaada taikina siihen. Paista 25–30 minuuttia, kunnes keskelle työnnetty tikku tulee puhtaana ulos.',
'Sulata kastiketta varten loput 25 g voita ja 60 g fariinisokeria kerman kanssa. Keitä hiljalleen 3 minuuttia sekoittaen. Lusikoi kastike kolmen lämpimän vanukasannoksen päälle ja tarjoa jäätelön kanssa.' ])
t('crumpets','Crumpetit, voi ja hillo','Kuusi pannulla paistettavaa aamiaisleipästä tavallisista vehnäjauhoista.','35 min + kohotus 1 h','6 crumpettia · 2 kullekin',[
'Sekoita jauhot, hiiva, sokeri ja suola kädenlämpöiseen maitoon ja 150 ml:aan kädenlämpöistä vettä. Peitä ja anna kohota tunti, kunnes taikina kuplii.',
'Sekoita leivinjauhe 15 ml:aan vettä ja vatkaa taikinaan. Taikinan tulee olla paksua mutta kaadettavaa. Lisää tarvittaessa hieman vettä.',
'Öljyä kevyesti tarttumaton paistinpannu ja metalliset paistorenkaat. Kuumenna melko miedolla lämmöllä. Aseta renkaat pannulle ja kaada niihin noin 1 cm:n kerros taikinaa. Paista 8–10 minuuttia, kunnes pinnalle muodostuu reikiä ja pinta on lähes hyytynyt.',
'Irrota renkaat varovasti. Käännä ja paista vielä 1–2 minuuttia. Tee yhteensä kuusi crumpettia. Ilman renkaita voit paistaa pienempiä, vapaamuotoisia leipäsiä: niistä tulee matalampia ja ne kypsyvät nopeammin. Tarjoa voin ja hillon kanssa.' ])
t('crumble','Omenapaistos ja vaniljakastike','Omenoita voi-jauhomurun alla.','45 min','Kolme annosta',[
'Lämmitä kiertoilmauuni 180 asteeseen. Poista omenoista siemenkodat ja viipaloi. Laita pieneen uunivuokaan 20 g sokerin, kanelin ja 30 ml:n vettä kanssa.',
'Nypi kylmä kuutioitu voi jauhoihin murumaiseksi seokseksi. Lisää loput 35 g sokeria. Ripottele omenoiden päälle painamatta pintaa tiiviiksi.',
'Paista 30–35 minuuttia, kunnes omenat ovat pehmeitä ja pinta kullanruskea. Anna vetäytyä 5 minuuttia.',
'Lämmitä vaniljakastike pakkauksen ohjeen mukaan ja tarjoa kolmen paistosannoksen kanssa.' ])
t('tomato-egg','Tomaatti-munapaistos','Tomaattia ja kananmunaa, jasmiiniriisiä ja kurkkusalaattia.','25 min','Kasvisruoka kaikille',[
'Keitä riisi pakkauksen ohjeen mukaan. Pilko kurkku suupaloiksi ja mausta murskatulla valkosipulilla, soijakastikkeella, riisiviinietikalla ja seesamiöljyllä.',
'Vatkaa kananmunat ja puolet suolasta kevyesti sekaisin. Kuumenna 15 ml öljyä suurella pannulla ja kypsennä munat varovasti sekoitellen juuri hyytyneeksi kokkeliksi. Siirrä lautaselle.',
'Pilko tomaatit ja kevätsipulit. Kuumenna loppu öljy. Lisää tomaatit, sokeri, loppu suola ja 50 ml vettä. Kypsennä 5–8 minuuttia, kunnes tomaatit ovat mehukkaita ja osittain hajonneet.',
'Kääntele kananmunat ja kevätsipulit joukkoon. Kuumenna minuutti ja tarjoa riisin sekä kurkkusalaatin kanssa.' ])
t('mapo','Mieto mapo-tyylinen tofu','Tofua ja sieniä misokastikkeessa, riisiä ja valkosipulilla paistettua paksoita.','35 min','Kasvisruoka kaikille',[
'Keitä riisi pakkauksen ohjeen mukaan. Kuutioi tofu noin 2 cm:n paloiksi. Hienonna sienet, inkivääri, valkosipuli ja kevätsipulit.',
'Kuumenna 15 ml öljyä laakealla pannulla. Paista sieniä 7 minuuttia, kunnes ne ruskistuvat. Lisää inkivääri, kaksi kolmasosaa valkosipulista ja kevätsipulien vaaleat osat. Sekoita minuutti.',
'Sekoita misotahna liemeen ja soijakastikkeeseen ja kaada pannulle. Lisää tofu ja hauduta varovasti 6–8 minuuttia. Sekoita maissitärkkelys 30 ml:aan kylmää vettä, kääntele kastikkeeseen ja keitä hiljalleen 2 minuuttia, kunnes kastike sakenee hieman. Lisää mustapippuri ja kevätsipulien vihreät osat.',
'Kuumenna toisella pannulla loput 10 ml öljyä ja loppu valkosipuli. Lisää pilkottu paksoi ja 30 ml vettä. Peitä 2 minuutiksi ja paista sitten ilman kantta 2 minuuttia. Tarjoa riisin kanssa. Laita chilirouhe erikseen pöytään.' ],'Tässä miedossa versiossa doubanjiang korvataan vegaanisella misotahnalla. Maku ja tulisuus poikkeavat perinteisestä sichuanilaisesta mapo tofusta. Myös kiinteä tofu käy, jos pehmeää ei ole saatavilla.')
t('char-siu','Char siu -tyylinen possu ja tofu','Hoisinilla maustettua uunipossua, erillinen tofuannos, riisiä ja paksoita.','65 min + marinointi 30 min','3 possuannosta + 1 tofuannos',[
'Leikkaa porsaanliha pitkiksi, noin 3 cm paksuiksi suikaleiksi ja tofu paksuiksi viipaleiksi. Sekoita hoisin, soijakastike, hunaja, kaneli, mustapippuri, raastettu inkivääri ja kaksi murskattua valkosipulinkynttä. Ota neljännes marinadista puhtaaseen kulhoon tofua varten. Marinoi liha ja tofu erikseen jääkaapissa vähintään 30 minuuttia.',
'Lämmitä kiertoilmauuni 190 asteeseen. Laita porsaanliha marinadeineen leivinpaperilla vuorattuun vuokaan ja tofu omaan pieneen vuokaansa. Paista lihaa 35–45 minuuttia ja käännä puolivälissä. Sisälämpötilan tulee olla vähintään 75 °C 30 sekunnin ajan. Paista tofua 25–30 minuuttia. Lisää tilkka vettä, jos marinadi alkaa palaa.',
'Keitä riisi pakkauksen ohjeen mukaan. Viipaloi paksoi. Kuumenna öljy pannulla ja paista loppua hienonnettua valkosipulia 30 sekuntia. Lisää paksoi ja 40 ml vettä. Peitä 2 minuutiksi ja jatka ilman kantta 2–3 minuuttia sekoitellen.',
'Anna lihan vetäytyä 5 minuuttia, viipaloi ja tarjoa riisin ja paksoin kanssa. Tarjoa tofu erikseen. Älä käytä raakaa lihaa koskettanutta, kypsentämätöntä marinadia pöytäkastikkeena.' ],'Valitse hoisinkastike, jonka ainesosissa ei ole maapähkinää. ”Saattaa sisältää maapähkinää” sopii tälle perheelle.')
t('chow-mein','Kana-kasvisnuudelit','Paistettuja nuudeleita ja kasviksia, yhdelle broilerin sijaan tofua.','30 min','3 kana-annosta + 1 tofuannos',[
'Keitä nuudelit pakkauksen ohjeen mukaan. Valuta ja sekoita seesamiöljy joukkoon. Suikaloi broileri, kuutioi tofu ja leikkaa kasvikset ohuiksi suikaleiksi. Sekoita soijakastike, hoisin ja 50 ml vettä kulhossa.',
'Paista broileria 10 ml:ssa öljyä 7–10 minuuttia, kunnes se on läpikypsää ja sisälämpötila vähintään 75 °C 30 sekunnin ajan. Siirrä sivuun. Ruskista tofu erillisellä pienellä pannulla 5 ml:ssa öljyä 6–8 minuuttia.',
'Kuumenna puhtaassa wokissa tai suuressa pannussa loput 15 ml öljyä. Paista hienonnettua valkosipulia ja inkivääriä 30 sekuntia. Lisää porkkanat, kaali ja paprika ja paista 5 minuuttia sekoitellen.',
'Lisää nuudelit, kastike ja kevätsipulit. Kääntele kuumaksi. Siirrä neljännes seoksesta tofupannulle. Lisää broileri suurempaan annokseen. Kuumenna molemmat ja tarjoa.' ])
t('jiaozi','Jiaozi-nyytit kahdella täytteellä','Itse tehdyt possu-kaali- ja sieni-kaalinyytit, kurkkusalaatti ja dippikastike.','90 min','24 possunyyttiä + 8 sieninyyttiä',[
'Sekoita 360 g vehnäjauhoa, ½ tl suolaa ja 190 ml lämmintä vettä kiinteäksi taikinaksi. Lisää tarvittaessa vettä lusikallinen kerrallaan. Vaivaa 8 minuuttia. Peitä ja anna levätä 30 minuuttia. Varaa loput 20 g jauhoa kaulimiseen.',
'Hienonna kaali ja sekoita loppu suola joukkoon. Anna seistä 10 minuuttia ja purista neste pois. Hienonna kevätsipuli, inkivääri ja yksi valkosipulinkynsi. Jaa nämä kasvikset kahteen kulhoon suhteessa 3:1. Lisää suurempaan annokseen porsaan jauheliha, 15 ml soijakastiketta ja 5 ml seesamiöljyä.',
'Hienonna sienet ja paista 5 ml:ssa rypsiöljyä, kunnes neste haihtuu. Anna jäähtyä. Lisää pienempään kasvisannokseen sekä 5 ml soijakastiketta ja 5 ml seesamiöljyä. Pidä täytteet ja niiden työvälineet erillään.',
'Jaa taikina 32 palaan ja kauli ohuiksi, halkaisijaltaan 10–11 cm:n ympyröiksi varatun jauhon avulla. Täytä 24 possuseoksella ja 8 sieniseoksella. Jaa täytteet tasan omien kuortensa kesken, noin kukkurallinen ruokalusikallinen kuhunkin. Nipistä tiiviisti kiinni. Taittele sieninyytit eri tavalla, jotta ne erottaa.',
'Kypsennä erissä erillisillä tarttumattomilla pannuilla. Jaa loput 25 ml rypsiöljyä paistoeriin. Paista pohjia 2 minuuttia. Lisää pannulle vettä noin 5 mm:n syvyydeltä ja peitä kannella. Höyrytä 8–10 minuuttia. Tarkista, että possutäytteen lämpötila on vähintään 75 °C 30 sekunnin ajan. Poista kansi ja anna veden haihtua, jotta pohjat rapeutuvat.',
'Sekoita dippiin 30 ml soijakastiketta, 30 ml riisiviinietikkaa ja 20 ml vettä. Murskaa kurkkua kevyesti ja pilko. Mausta lopulla 10 ml:lla soijakastiketta, 10 ml:lla etikkaa, 5 ml:lla seesamiöljyä ja murskatulla valkosipulinkynnellä. Tarjoa nyyttien kanssa.' ],'Kuoret tehdään tavallisesta vehnäjauhosta. Taittele sieninyytit ensin. Kypsentämiseen riittää leveä paistinpannu ja tiivis kansi.')
t('gong-bao','Gong bao -tyylinen kana ilman maapähkinöitä','Kana-paprikawokki kirpeänmakeassa kastikkeessa, yhdelle tofuversio.','35 min','3 kana-annosta + 1 tofuannos',[
'Keitä riisi pakkauksen ohjeen mukaan. Kuutioi broileri ja tofu. Sekoita soijakastike, riisiviinietikka, sokeri, maissitärkkelys ja 120 ml vettä. Ota neljännes puhtaasta kastikkeesta talteen tofupannua varten.',
'Ruskista tofu pienellä pannulla 5 ml:ssa öljyä 6–8 minuuttia. Paista broileria suuremmalla pannulla 10 ml:ssa öljyä 7–10 minuuttia, kunnes sisälämpötila on vähintään 75 °C 30 sekunnin ajan. Siirrä molemmat sivuun omiin kulhoihinsa.',
'Pilko paprikat ja porkkanat pieniksi paloiksi. Paista puhtaalla pannulla lopussa 15 ml:ssa öljyä 5 minuuttia sekoitellen. Lisää hienonnettu inkivääri, valkosipuli ja kevätsipulit. Paista vielä minuutti.',
'Jaa kasvikset kana- ja tofupannuihin suhteessa 3:1. Sekoita kumpikin kastikeannos ennen pannulle lisäämistä. Keitä hiljalleen 2–3 minuuttia, kunnes kastike sakenee ja ruoka on kauttaaltaan kuumaa. Tarjoa riisin kanssa ja chilirouhe erikseen.' ],'Maapähkinät jätetään pois eikä niitä korvata muilla pähkinöillä.')
t('hot-pot','Hot pot','Yhteinen kasvisliemi, tofua, kasviksia ja nuudeleita. Naudanliha kypsennetään omassa kattilassaan.','45 min + kypsentäminen ruokailun aikana','Kasviskattila kaikille + naudanlihaa kolmelle',[
'Varaa kaksi kattilaa, erilliset kauhat ja pihdit sekä turvallinen pöytäkeitin. Voit myös pitää kattilat liedellä ja tarjoilla kypsät erät pöytään. Pidä raa’an lihan lautanen ja työvälineet erillään kypsästä ruoasta.',
'Hauduta kasvislientä, viipaloitua inkivääriä, kahta murskattua valkosipulinkynttä ja puolta kevätsipulista 15 minuuttia. Siirrä 750 ml lientä lihakattilaan ja jätä 1,75 litraa yhteiseen kattilaan. Pidä molemmat hiljalleen kiehuvina.',
'Viipaloi sienet, pese ja pilko paksoi sekä kiinankaali, leikkaa porkkanat hyvin ohuiksi ja kuutioi tofu. Asettele tarjoiluastioihin. Säilytä ohuiksi viipaloitu raaka naudanliha jääkaapissa kypsentämiseen asti. Keitä nuudelit erikseen pakkauksen ohjeen mukaan ja jaa kulhoihin.',
'Sekoita soijakastike, riisiviinietikka ja seesamiöljy 50 ml:aan vettä. Lisää loput hienonnetusta valkosipulista ja kevätsipulista. Jaa dippikulhoihin. Tarjoa seesaminsiemenet ja chilirouhe erikseen.',
'Kypsennä sieniä ja porkkanoita pienissä erissä yhteisessä kattilassa 4–6 minuuttia. Lisää lehtikasvikset ja tofu ja kypsennä vielä 3–5 minuuttia kuumiksi ja pehmeiksi. Kypsennä naudanliha vain omassa kattilassaan pienissä erissä kauttaaltaan kypsäksi. Tarkista taitetun paksun palan lämpötilaksi vähintään 75 °C 30 sekunnin ajan. Pelkkä nopea kastaminen liemeen ei riitä.',
'Tarjoa kypsät ainekset nuudelien ja dippikastikkeiden kanssa. Lisää kattiloihin kuumaa vettä liemen haihtuessa. Pidä molemmat liemet hiljalleen kiehuvina koko ruokailun ajan. Käytä syömiseen puhtaita välineitä, älä raa’an lihan pihtejä.' ],'Määrissä on naudanlihaa kolmelle ja tofua kaikille neljälle. Liemi on mieto; jokainen voi maustaa oman dippinsä.')
t('congee','Congee-riisipuuro','Suolaista riisipuuroa, kananmunia, kevätsipulia ja rapeaksi paistettua sipulia.','65 min','Kasvisruoka kaikille',[
'Huuhtele riisi. Laita suureen kattilaan 1,5 litran vettä, viipaloidun inkiväärin ja suolan kanssa. Kiehauta ja hauduta osittain kannen alla 50–60 minuuttia välillä sekoittaen, kunnes puuro on pehmeää. Lisää kuumaa vettä, jos puuro sakenee liikaa.',
'Keitä kananmunia 9–10 minuuttia. Jäähdytä kylmän veden alla, kuori ja puolita. Viipaloi sipuli ohuesti ja paista rypsiöljyssä 10–15 minuuttia kullanruskeaksi. Valuta talouspaperilla.',
'Poista inkivääriviipaleet. Jaa puuro neljään kulhoon ja lisää päälle kananmunat, rapea sipuli ja hienonnettu kevätsipuli.',
'Sekoita soijakastike ja seesamiöljy. Anna kunkin lisätä seosta omaan annokseensa.' ])
t('mango-pudding','Mango-kookosvanukas','Neljä agarilla hyydytettyä jälkiruoka-annosta ilman liivatetta.','20 min + jäähdytys 3 h','Sama jälkiruoka kaikille',[
'Soseuta sulatettu mango sileäksi ja anna lämmetä huoneenlämpöiseksi. Sosetta tarvitaan noin 300 ml.',
'Vatkaa agarjauhe ja sokeri kookosmaitoon kattilassa. Kuumenna kiehuvaksi sekoittaen ja keitä hiljalleen 2 minuuttia, jotta agar liukenee. Noudata tuotteen omaa käyttöohjetta, jos se poikkeaa tästä.',
'Vatkaa mangosose nopeasti joukkoon miedolla lämmöllä, kunnes seos on tasaista ja höyryävän kuumaa. Älä anna jäähtyä kattilassa. Jaa neljään pieneen lasiin.',
'Anna jäähtyä ja siirrä jääkaappiin vähintään 3 tunniksi hyytymään. Tarjoa kylmänä laseista.' ],'Käytä puhdasta agarjauhetta, ei makeutettua hyytelöimisaineseosta. Vahvuus vaihtelee: noudata pakkauksen annostusta noin 550 ml:lle seosta, jos se poikkeaa ohjeesta. K-Ruoan valikoimassa on Meiran agar-agaria.')
t('scallion-pancakes','Kevätsipulipannukakut','Neljä suolaista pannukakkua ja dippikastike kevyeksi lounaaksi.','50 min','4 pannukakkua',[
'Sekoita 300 g jauhoa ja suola. Lisää varovasti 180 ml vastakiehautettua vettä. Kun taikinaa voi käsitellä, vaivaa 5 minuuttia sileäksi. Peitä ja anna levätä 20 minuuttia. Varaa loput 20 g jauhoa kaulimiseen.',
'Jaa neljään osaan. Kauli kukin ohueksi suorakulmioksi. Jaa 25 ml öljyä levyjen voiteluun ja ripottele päälle hienonnettu kevätsipuli. Rullaa pötköksi, kierrä spiraaliksi ja litistä varovasti. Anna levätä 5 minuuttia ja kauli halkaisijaltaan 16–18 cm:n levyiksi.',
'Jaa loput 30 ml öljyä paistamiseen. Paista pannukakkuja keskilämmöllä 3–4 minuuttia kummaltakin puolelta, kunnes ne ovat kullanruskeita ja sisältä kypsiä. Paina kevyesti lastalla paistamisen aikana.',
'Sekoita soijakastike, riisiviinietikka, seesamiöljy ja 20 ml vettä. Leikkaa pannukakut lohkoiksi ja tarjoa dipin kanssa.' ])
t('sesame-biscuits','Seesamikeksit ja vaniljajäätelö','Helppo vaihtoehto seesamipalloille, ilman erikoisjauhoja.','30 min','Noin 12 keksiä neljälle',[
'Lämmitä kiertoilmauuni 170 asteeseen. Vatkaa pehmeä voi ja sokeri vaahdoksi. Sekoita jauhot, leivinjauhe ja 25 g seesaminsiemeniä. Lisää voiseokseen maidon kanssa ja sekoita pehmeäksi taikinaksi.',
'Jaa kahteentoista palloon ja litistä leivinpaperilla vuoratulle pellille. Jätä keksien väliin tilaa. Painele loput 15 g seesaminsiemeniä pintaan.',
'Paista 14–18 minuuttia, kunnes reunat ovat vaalean kullanruskeat. Anna jäähtyä pellillä 5 minuuttia ja siirrä sitten ritilälle.',
'Tarjoa kolme keksiä kullekin vaniljajäätelön kanssa.' ],'Seesamikeksit korvaavat aiemmin suunnitellut seesamipallot. Resepti sisältää seesamia; maapähkinää ei käytetä.')

def localize(catalog, recipes):
    used={i['key'] for r in recipes for i in r['ingredients']}
    assert used <= LABELS.keys(), used-LABELS.keys()
    assert {r['id'] for r in recipes} == TEXT.keys()
    for key,item in catalog.items():
        if key in LABELS:item['label']=LABELS[key]
        item['group']=GROUPS.get(item['group'],item['group'])
    for r in recipes:r.update(TEXT[r['id']])
SHOP_NOTES={
'garlic':'Määrät ovat kynsiä, eivät kokonaisia valkosipuleita. Yhdessä valkosipulissa on yleensä noin 8–10 kynttä.',
'whitebean':'Paino on valutettuna. 400 g:n tölkistä saa usein noin 240 g papuja; tarkista pakkauksesta.',
'lentil':'Määrä tarkoittaa kypsiä, valutettuja linssejä. Osta säilyke- tai pussilinssejä, älä tätä määrää kuivia linssejä.',
'filo':'Kreikan viikolla tarvitaan yhteensä 450 g, joten yksi 500 g:n pakkaus riittää. Sulata ja säilytä pakkauksen mukaan. Tarvittaessa paista ja pakasta sunnuntain piiraat etukäteen.',
'orzo':'Jos orzoa ei ole, käytä sama kuivapaino pientä makaronia. Noudata sen kypsymisaikaa ja tarkista nesteen riittävyys paiston aikana.',
'paneer':'Voit korvata paneerin samalla grammamäärällä kiinteää tofua.',
'softtofu':'Kiinteä maustamaton tofu käy samalla grammamäärällä. Rakenteesta tulee kiinteämpi.',
'pakchoi':'Voit käyttää saman grammamäärän kiinankaalia. Kypsennä paksummat varret ensin.',
'hotbeef':'Pyydä lihatiskiltä hyvin ohuita viipaleita. Voit myös kohmettaa kokonaisen vähärasvaisen lihapalan lyhyesti pakastimessa ennen viipalointia.',
'cod':'Maustamatonta turskaa tai koljaa. Ei lohta, kirjolohta, savukalaa eikä kalasekoituksia.',
'hoisin':'Tarkista, ettei ainesosissa ole maapähkinää. ”Saattaa sisältää maapähkinää” sopii tälle perheelle.',
'beanpaste':'Valitse vegaaninen misotahna, jonka ainesosissa ei ole maapähkinää. Miso korvaa tässä miedossa reseptissä doubanjiangin.',
'agar':'Puhdas jauhe; noudata pakkauksen annostusohjetta. Älä korvaa liivatteella.',
'oil':'Rypsiöljyä, ei maapähkinäöljyä. Sekä Kreikan että Britannian listassa on mukana kokonainen uppopaistoöljyerä.',
'stock':'Määrä tarkoittaa valmista lientä. Osta riittävästi kuutioita tai tiivistettä ja laimenna pakkauksen ohjeen mukaan.',
'mango':'Paino tarkoittaa hedelmälihaa. Pakastemangoa käyttäessä ei tarvitse huomioida kuorta ja kiveä.',
'cauliflower':'Paino on puhdistettuja kukintoja. Kokonaisena ostettaessa huomioi lehdet ja kanta.',
'icecream':'Määrät ovat grammoja, eivät millilitroja. Tarkista pakkauksen nettopaino.',
'malt':'Jos mallasetikkaa ei ole, käytä sama määrä omenaviinietikkaa. Maku on hieman erilainen.',
'cheddar':'Valitse ruokavalioon sopiva juusto. Cheddar korvaa myös Kreikan viikon erikoisjuuston.',
}
