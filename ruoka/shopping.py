"""Finnish search terms and checked K-Ruoka catalogue examples (2026-09-11)."""
STORE='https://www.k-ruoka.fi/kauppa/k-citymarket-helsinki-ruoholahti'
FI=dict(potato='peruna',onion='sipuli',redonion='punasipuli',tomato='tomaatti',cucumber='kurkku',carrot='porkkana',celery='varsiselleri',spinach='pinaatti pakaste',aubergine='munakoiso',mushroom='herkkusieni',leek='purjo',salad='salaattisekoitus',pepper='paprika',cabbage='kiinankaali',pakchoi='paksoi',cauliflower='kukkakaali',ginger='inkivääri',spring='kevätsipuli',apple='omena',mango='mango pakaste',lemon='sitruuna',garlic='valkosipuli',dill='tilli',parsley='persilja',chicken='kana maustamaton',beef='naudan palapaisti',mince='naudan jauheliha',pork='porsaan kassler',porkmince='porsaan jauheliha',hotbeef='naudan paisti',prawn='raaka kuorittu katkarapu',cod='turskafilee',tofu='tofu maustamaton',softtofu='pehmeä tofu',halloumi='halloumi',paneer='paneer',sausage='raakamakkara',vegsausage='kasvismakkara',bacon='pekoni',feta='feta',yogurt='kreikkalainen jogurtti',butter='voi',cheddar='cheddar',hardcheese='cheddar',milk='maito',cream='kuohukerma',egg='kananmuna',bread='leipä',filo='filotaikina',pita='pitaleipä',naan='naanleipä',whitebean='valkoiset pavut',lentil='vihreät linssit säilyke',tintomato='tomaattimurska',puree='tomaattipyree',peas='herne pakaste',bakedbeans='valkoiset pavut tomaattikastikkeessa',icecream='vaniljajäätelö',coconut='kookosmaito',custard='vaniljakastike',orzo='orzo',rice='jasmiiniriisi',basmati='basmatiriisi',noodles='vehnänuudeli',flour='vehnäjauho',cornflour='maissitärkkelys',sugar='sokeri',brownsugar='fariinisokeri',date='taateli kivetön',sesame='seesaminsiemen',baking='leivinjauhe',bicarb='ruokasooda',yeast='kuivahiiva',vanilla='vaniljauute',agar='agar agar',olive='oliiviöljy',oil='rypsiöljy',soy='soijakastike',vinegar='riisiviinietikka',sesameoil='seesamiöljy',malt='mallasetikka',honey='hunaja',jam='hillo',mustard='dijon sinappi',mayo='majoneesi',caper='kapris',gherkin='maustekurkku',hoisin='hoisin kastike',chilli='chilirouhe',beanpaste='miso tahna',stock='kasvisliemi',salt='suola',blackpepper='mustapippuri',oregano='oregano',cinnamon='kaneli',nutmeg='muskottipähkinä',cumin='juustokumina',coriander='korianteri jauhettu',garam='garam masala',paprika='paprikajauhe',turmeric='kurkuma',thyme='timjami',bay='laakerinlehti')
PRODUCTS={
'filo':('Myllyn Paras filotaikina 500 g','myllyn-paras-filotaikina-500g-6417700063596'),
'orzo':('Filos orzo jyväpasta 500 g','filos-orzo-jyvapasta-500g-6416710060069'),
'paneer':('Apetina Paneer 225 g','apetina-paneer-225g-ruoanlaittojuusto-5711953081699'),
'hoisin':('Spice Up Hoi sin kastike 260 g','spice-up-hoi-sin-kastike-260g-6430011813346'),
'beanpaste':('House of Asia Miso paste 120 g dark dashi (tuotetiedoissa vegaaninen)','house-of-asia-miso-paste-120g-dark-dashi-5904358553537'),
'agar':('Meira Agar Agar 60 g','meira-agar-agar-60g-hyyteloimisjauhe-6420101883564'),
}
# These are planning pack sizes, not a claim about current stock or exact products.
PACKS=dict(filo=500,orzo=500,paneer=225,whitebean=240,lentil=240,tintomato=400,tofu=250,softtofu=300,feta=200,halloumi=200,milk=1000,cream=200,coconut=250,flour=1000,rice=1000,basmati=1000,oil=1000,hoisin=260,beanpaste=120,agar=60,egg=10,peas=200,spinach=150,naan=2,pita=4,butter=500,cheddar=200,hardcheese=200)
NOTES={
'garlic':'Counts are cloves, not bulbs; allow roughly 8–10 cloves per bulb.',
'whitebean':'Weight is drained: a 400 g tin often yields about 240 g. Check the label.',
'lentil':'Ready-cooked, drained weight. Buy tinned or pouched lentils, not dry lentils for these quantities.',
'filo':'450 g across Greece week fits one 500 g pack. Thaw and store according to the pack; bake and freeze Sunday’s parcels early if needed.',
'orzo':'If unavailable, use the same dry weight of small macaroni; follow its cooking time and check liquid as it bakes.',
'paneer':'Firm tofu works gram-for-gram if paneer is unavailable.',
'softtofu':'Firm plain tofu works gram-for-gram; the texture will be less delicate.',
'pakchoi':'Chinese cabbage works gram-for-gram; cook thicker stems first.',
'hotbeef':'Ask the meat counter to slice very thinly, or briefly firm up a whole lean cut in the freezer before slicing.',
'cod':'Plain cod or haddock only. No salmon, trout, smoked fish or mixed fish packs.',
'hoisin':'Check the current ingredient label for peanuts. A “may contain peanuts” warning is acceptable for this household.',
'beanpaste':'Choose vegan miso with no peanut ingredients. Miso is the explicit mild substitute for doubanjiang in this plan.',
'agar':'Pure powder; follow its setting ratio. Do not substitute gelatine in the meat-free pudding.',
'oil':'Rapeseed oil, not peanut/groundnut oil. Greece and UK totals each include a full frying batch.',
'stock':'Quantity is prepared stock. Buy cubes or concentrate sufficient for that volume; use the packet dilution ratio.',
'mango':'Weight is usable flesh; frozen mango avoids peel and stone allowances.',
'cauliflower':'Trimmed florets weight; allow extra for leaves and core when buying whole heads.',
'icecream':'Amounts are grams, not millilitres. Check net weight when choosing a tub.',
'malt':'If unavailable, use the same volume of apple cider vinegar; the flavour will differ.',
'cheddar':'Choose cheese suitable for the meat-free diner; cheddar also replaces specialist Greek hard cheese.',
}
