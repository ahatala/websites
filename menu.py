"""Family menu and quantities. Run python3 build.py after editing."""
CAT = {}
def catalog(group, unit, entries):
    for key, label in entries.items(): CAT[key] = dict(label=label, unit=unit, group=group)
catalog('Vegetables & fruit','g', dict(potato='Potatoes', onion='Onions', redonion='Red onions', tomato='Tomatoes', cucumber='Cucumber', carrot='Carrots', celery='Celery', spinach='Frozen chopped spinach', aubergine='Aubergines', mushroom='Mushrooms', leek='Leeks', salad='Salad leaves', pepper='Bell peppers', cabbage='Chinese cabbage', pakchoi='Pak choi', broccoli='Broccoli', cauliflower='Cauliflower (trimmed)', ginger='Fresh ginger', spring='Spring onions', apple='Apples', mango='Mango flesh (fresh or frozen)', beansprout='Bean sprouts'))
catalog('Vegetables & fruit','whole', dict(lemon='Lemons', garlic='Garlic cloves'))
catalog('Vegetables & fruit','g', dict(dill='Fresh dill', parsley='Fresh parsley'))
catalog('Meat, fish & alternatives','g', dict(chicken='Boneless chicken', beef='Stewing beef', mince='Minced beef', pork='Pork shoulder, boneless', porkmince='Minced pork', hotbeef='Thinly sliced beef for hot pot', prawn='Raw peeled prawns', cod='Boneless cod or haddock fillets', tofu='Firm tofu', softtofu='Soft tofu', halloumi='Halloumi', paneer='Paneer', sausage='Pork sausages', vegsausage='Vegetarian sausages', bacon='Bacon'))
catalog('Dairy & eggs','g', dict(feta='Feta', yogurt='Greek yogurt', butter='Butter', cheddar='Cheddar', hardcheese='Cheddar (for Greek bakes)'))
catalog('Dairy & eggs','ml', dict(milk='Milk', cream='Double cream'))
catalog('Dairy & eggs','whole', dict(egg='Eggs'))
catalog('Bakery & chilled','g', dict(bread='Crusty / sliced bread', filo='Filo pastry', wrapper='Dumpling wrappers'))
catalog('Bakery & chilled','pieces', dict(pita='Pita breads', naan='Naan breads', crumpet='Crumpets'))
catalog('Tins & freezer','g drained', dict(whitebean='Tinned white beans', lentil='Tinned green or brown lentils'))
catalog('Tins & freezer','g', dict(tintomato='Tinned chopped tomatoes', puree='Tomato purée', peas='Frozen peas', bakedbeans='Baked beans', icecream='Vanilla ice cream', redbean='Sweet red-bean paste (no peanut ingredients)'))
catalog('Tins & freezer','ml', dict(coconut='Coconut milk', custard='Ready-made custard'))
catalog('Rice, flour & baking','g', dict(orzo='Orzo (dry)', rice='Jasmine rice (dry)', basmati='Basmati rice (dry)', noodles='Wheat noodles (dry)', flour='Plain flour', cornflour='Cornflour', riceflour='Glutinous rice flour', sugar='Caster sugar', brownsugar='Brown sugar', date='Pitted dates', sesame='Sesame seeds'))
catalog('Rice, flour & baking','tsp', dict(baking='Baking powder', bicarb='Bicarbonate of soda', yeast='Instant dried yeast', vanilla='Vanilla extract'))
catalog('Rice, flour & baking','g', dict(agar='Agar-agar powder'))
catalog('Oils, sauces & pantry','ml', dict(olive='Olive oil', oil='Rapeseed oil (including frying oil)', soy='Light soy sauce', darksoy='Dark soy sauce', vinegar='Chinkiang black vinegar', sesameoil='Toasted sesame oil', malt='Malt vinegar'))
catalog('Oils, sauces & pantry','g', dict(honey='Honey', jam='Jam', mustard='Dijon mustard', mayo='Mayonnaise', caper='Capers', gherkin='Gherkins', hoisin='Hoisin sauce (no peanut ingredients)', douban='Doubanjiang (no peanut ingredients)', chilli='Chilli flakes (serve separately)', beanpaste='Mild fermented soybean paste'))
catalog('Oils, sauces & pantry','ml prepared', dict(stock='Vegetable stock (from cubes or concentrate)'))
catalog('Oils, sauces & pantry','ml', dict(worcester='Vegetarian Worcestershire sauce'))
catalog('Spices & seasoning','tsp', dict(salt='Salt', blackpepper='Black pepper', oregano='Dried oregano', cinnamon='Ground cinnamon', nutmeg='Ground nutmeg', cumin='Ground cumin', coriander='Ground coriander', garam='Garam masala', paprika='Paprika', turmeric='Turmeric', thyme='Dried thyme', five='Chinese five-spice', sichuan='Ground Sichuan pepper'))
catalog('Spices & seasoning','whole', dict(bay='Bay leaves'))
RECIPES=[]
def add(id, week, day, kind, title, desc, servings, time, split, ingredients, steps, note=''):
    parsed=[]
    for part in ingredients.split(';'):
        key, qty=part.strip().split(':'); assert key in CAT,key
        parsed.append(dict(key=key, qty=float(qty)))
    RECIPES.append(dict(id=id,week=week,day=day,kind=kind,title=title,desc=desc,servings=servings,time=time,split=split,ingredients=parsed,steps=steps,note=note))
add('souvlaki','greece','Monday','Dinner','Souvlaki night','Warm pitas, lemony chicken, golden halloumi and a table full of toppings.',4,'40 min + 20 min marinating','3 chicken + 1 halloumi',
'chicken:450; halloumi:150; pita:4; yogurt:250; cucumber:400; tomato:400; redonion:100; lemon:1; garlic:2; olive:30; oregano:2; salt:0.75; blackpepper:0.25',[
'Cube the chicken. Mix olive oil, half the lemon juice, 1 crushed garlic clove, oregano, half the salt and the pepper. Reserve one quarter in a clean bowl for the halloumi; coat the chicken in the rest and refrigerate for 20 minutes.',
'Grate 150 g cucumber, squeeze dry and mix with the yogurt, remaining garlic, remaining lemon juice and salt to make tzatziki. Slice the remaining cucumber, tomatoes and onion.',
'Thread chicken onto skewers (soak wooden skewers first). Grill or pan-fry over medium-high heat for 10–14 minutes, turning, until the centre reaches 75°C for 30 seconds.',
'Cut halloumi into thick pieces, coat in its reserved marinade and cook in a separate pan for 2–3 minutes per side. Warm the pitas and assemble with tzatziki and vegetables.' ])
add('spanakopita','greece','Tuesday','Dinner','Spanakopita & Greek salad','A crackly spinach-and-feta pie for the whole table.',4,'65 min','Meat-free for everyone',
'spinach:600; feta:300; filo:250; egg:2; onion:150; dill:15; olive:60; tomato:400; cucumber:300; redonion:75; lemon:0.5; oregano:1; salt:0.5; blackpepper:0.5',[
'Heat the oven to 180°C fan. Thaw the spinach and squeeze it very dry. Chop the onion and soften in 15 ml oil for 8 minutes; let cool slightly.',
'Mix spinach, onion, 200 g crumbled feta, eggs, chopped dill, pepper and half the salt. Brush a roughly 20 × 25 cm dish with a little of 30 ml oil. Layer half the filo in it, brushing lightly between sheets. Keep unused filo under a damp towel.',
'Add the filling, cover with the remaining filo and brush with the rest of that 30 ml oil. Tuck in the edges, score the top into four portions and bake for 35–40 minutes until crisp and the filling is set.',
'Chop tomatoes, cucumber and red onion. Dress with the remaining 15 ml oil, lemon juice, oregano and salt. Top with the remaining 100 g feta and serve with the pie.' ])
add('fasolada','greece','Wednesday','Dinner','Fasolada','White beans, tomato and vegetables, with bread and feta.',4,'45 min','Meat-free for everyone',
'whitebean:720; tintomato:400; onion:150; carrot:250; celery:150; garlic:2; olive:30; stock:800; oregano:1; bay:1; bread:400; feta:150; salt:0.5; blackpepper:0.5',[
'Dice the onion, carrots and celery. Soften in the olive oil in a large saucepan for 10 minutes. Add chopped garlic and stir for 1 minute.',
'Add tomatoes, drained beans, prepared vegetable stock, oregano and bay leaf. Bring to a simmer and cook gently for 25 minutes until the carrots are tender.',
'Mash a ladleful of beans against the side of the pan to thicken the soup. Remove the bay leaf. Season with salt and pepper, reducing the salt if the stock is already salty.',
'Warm the bread and serve with bowls of soup and crumbled feta on the side.' ],'720 g drained beans is about three 400 g tins; check the drained weights.')
add('giouvetsi','greece','Thursday','Dinner','Beef giouvetsi','Slow-cooked beef and tomato orzo, just for the three attending.',3,'2 hr 30 min','3 beef portions · meat-free diner away',
'beef:600; orzo:240; tintomato:400; onion:150; garlic:2; olive:20; puree:20; stock:700; cinnamon:0.5; bay:1; hardcheese:40; salt:0.5; blackpepper:0.5',[
'Heat the oven to 160°C fan. Cut beef into 3 cm cubes. Brown in the oil in an ovenproof casserole in batches, then lift out. Soften chopped onion in the same pot for 8 minutes.',
'Add chopped garlic and tomato purée; stir for 1 minute. Return the beef with tomatoes, 400 ml stock, cinnamon, bay, salt and pepper. Cover and bake for 1½–2 hours until fork-tender.',
'Raise the oven to 180°C fan. Remove the bay leaf. Stir in the dry orzo and remaining 300 ml hot stock. Bake uncovered for 20–25 minutes, stirring halfway. Add a splash of hot water if the orzo is drying out before it is tender.',
'Rest for 10 minutes; the orzo continues absorbing sauce. Serve with grated hard cheese.' ])
add('saganaki','greece','Friday','Dinner','Prawn saganaki','Prawns in a rich tomato sauce, with feta, bread and Greek salad.',4,'35 min','Shared seafood meal',
'prawn:600; tintomato:800; onion:150; garlic:3; feta:200; olive:40; oregano:1; parsley:15; bread:400; tomato:300; cucumber:300; redonion:75; lemon:1; salt:0.5; blackpepper:0.5',[
'Heat the oven to 200°C fan. Soften chopped onion in 25 ml oil in an ovenproof frying pan for 8 minutes. Add chopped garlic and oregano for 1 minute, then tinned tomatoes, salt and pepper. Simmer for 12–15 minutes until thickened.',
'Pat the thawed, peeled prawns dry. Stir into the sauce, crumble 150 g feta over the top and bake for 8–12 minutes until the prawns are opaque throughout and cooked through.',
'Chop fresh tomatoes, cucumber and red onion. Dress with the remaining 15 ml oil and half the lemon juice; top with the remaining 50 g feta.',
'Sprinkle chopped parsley over the prawns. Serve with bread, salad and the remaining lemon cut into wedges.' ])
add('moussaka','greece','Sunday','Dinner','Moussaka, two ways','One beef bake and one small lentil-and-mushroom bake, with shared layers.',4,'1 hr 50 min','3 beef + 1 lentil & mushroom',
'aubergine:800; potato:600; mince:450; lentil:120; mushroom:100; tintomato:600; onion:200; garlic:3; puree:20; olive:60; cinnamon:0.5; oregano:1; butter:50; flour:50; milk:600; hardcheese:60; nutmeg:0.25; salt:1; blackpepper:0.5',[
'Heat the oven to 200°C fan. Slice potatoes and aubergines into 5 mm rounds. Toss with 45 ml oil and half the salt. Roast on lined trays for 25–30 minutes, turning once, until tender.',
'Soften chopped onion in the remaining 15 ml oil for 8 minutes. Add garlic and purée for 1 minute, then tomatoes, cinnamon, oregano, remaining salt and pepper. Simmer for 15 minutes. Divide this meat-free sauce: three quarters into one bowl, one quarter into another.',
'Brown the beef in a large pan for 8–10 minutes, breaking it up; stir in the larger sauce portion and simmer for 10 minutes. In a separate small pan, dry-fry chopped mushrooms until their liquid evaporates, then add drained lentils and the smaller sauce portion; simmer for 5 minutes.',
'Melt butter in a saucepan, stir in flour and cook for 1 minute. Gradually whisk in milk. Simmer, whisking, until thick; stir in nutmeg and half the cheese.',
'Reduce the oven to 180°C fan. Use a roughly 20 × 20 cm dish for the beef and a small 12 × 15 cm dish for the meat-free portion. Split potatoes, aubergines and béchamel 3:1 between them. Layer potatoes, aubergine, filling and béchamel; finish with remaining cheese.',
'Bake for 35–40 minutes until bubbling, golden and hot throughout (beef filling 75°C for 30 seconds). Rest for 15 minutes before serving.' ])
add('tiropita','greece','Sunday','Lunch / snack','Little tiropita','Golden feta parcels; eight small pies for four.',4,'40 min','Meat-free for everyone',
'filo:200; feta:200; yogurt:80; egg:1; butter:40; blackpepper:0.25',[
'Heat the oven to 180°C fan. Mash feta with yogurt, egg and pepper. Melt the butter.',
'Cut filo into strips about 10 cm wide. Use two layers for each of eight parcels, brushing lightly with butter. Keep the remaining pastry covered with a damp towel.',
'Put one eighth of the filling at one end of each strip. Fold a corner over into a triangle, then continue folding to the end, enclosing the filling.',
'Brush with remaining butter and bake on a lined tray for 20–25 minutes until golden and the filling is set. Cool for 5 minutes.' ])
add('loukoumades','greece','Sunday','Dessert','Loukoumades','A small batch of warm honey-and-cinnamon doughnuts.',4,'35 min + 1 hr rising','Makes about 16 small doughnuts',
'flour:200; yeast:1; sugar:10; salt:0.25; oil:750; honey:80; cinnamon:1',[
'Mix flour, yeast, sugar and salt. Beat in 200 ml lukewarm water to make a thick, sticky batter. Cover and leave in a warm place for about 1 hour until bubbly and doubled.',
'Warm honey with 20 ml water in a small pan; set aside. Heat rapeseed oil to 175°C in a deep heavy pan no more than one third full. Use a thermometer and keep children away from the frying area.',
'Using two damp teaspoons, gently lower small spoonfuls of batter into the oil. Fry in batches for 3–4 minutes, turning, until golden and cooked inside. Keep the oil around 175°C and drain on kitchen paper.',
'Toss with the honey syrup, sprinkle with cinnamon and serve warm.' ],'Frying oil is counted as a whole batch in the shopping list, not as the amount eaten. Use a narrower suitable pot if 750 ml does not give enough depth; never overfill.')
add('tikka','uk','Monday','Dinner','Chicken & paneer tikka masala','One gently spiced sauce, two pans, rice and warm naan.',4,'45 min','3 chicken + 1 paneer',
'chicken:450; paneer:150; yogurt:100; onion:200; garlic:3; ginger:20; tintomato:400; cream:150; oil:30; garam:2; cumin:1; coriander:1; paprika:1; turmeric:0.5; salt:0.75; basmati:300; naan:4',[
'Cook the rice according to its packet. Dice the onion and soften in 15 ml oil for 8 minutes. Add grated ginger, crushed garlic and all the spices; stir for 1 minute.',
'Add tomatoes and salt, simmer for 15 minutes, then stir in cream and yogurt over low heat. Divide this meat-free sauce between two pans, three quarters for chicken and one quarter for paneer.',
'Cube the chicken. Brown in 10 ml oil for 5 minutes, add to its sauce and simmer for 12–15 minutes until cooked through, reaching 75°C for 30 seconds in the centre.',
'Cube paneer and brown in the remaining 5 ml oil in a separate pan for 5 minutes. Add to its sauce and simmer for 5 minutes. Warm naan according to the packet and serve with rice.' ],'Paneer can be replaced gram-for-gram with firm tofu if it is missing from the cheese shelf.')
add('cottage','uk','Tuesday','Dinner','Lentil & mushroom cottage pie','A deeply savoury filling under a fork-ridged potato roof.',4,'65 min','Meat-free for everyone',
'lentil:480; mushroom:400; onion:200; carrot:250; garlic:2; puree:30; stock:400; soy:15; thyme:1; flour:20; olive:25; potato:1000; milk:150; butter:40; cheddar:60; salt:0.75; blackpepper:0.5',[
'Heat the oven to 190°C fan. Peel and chop potatoes. Boil for 15–20 minutes until tender; drain and mash with milk, butter and half the salt.',
'Dice onions and carrots and soften in olive oil for 8 minutes. Add chopped mushrooms and cook for 8 minutes until their liquid evaporates. Add garlic, thyme and tomato purée, then flour; stir for 1 minute.',
'Stir in stock, drained lentils, soy sauce, pepper and remaining salt. Simmer for 10 minutes until thick. Spoon into a roughly 20 × 25 cm baking dish.',
'Spread mash over the filling, roughen with a fork and scatter with grated cheddar. Bake for 25 minutes until bubbling and golden.' ])
add('leek-soup','uk','Wednesday','Dinner','Leek & potato soup','A cosy bowl with crisp cheddar toasties for dunking.',4,'40 min','Meat-free for everyone',
'leek:500; potato:500; onion:150; butter:50; stock:1000; milk:200; bread:400; cheddar:200; salt:0.5; blackpepper:0.5',[
'Wash leeks carefully and slice. Chop onion and soften both in 25 g butter for 10 minutes without browning.',
'Add peeled, diced potatoes and stock. Simmer for 20 minutes until very tender. Blend until smooth, stir in milk, salt and pepper, and warm through gently.',
'Make four sandwiches with bread and cheddar. Spread the remaining 25 g butter thinly on the outsides. Pan-toast over medium-low heat for 3–4 minutes per side until golden and melted inside.',
'Cut the toasties into fingers or triangles and serve with the soup.' ])
add('fish-chips','uk','Thursday','Dinner','Fish & chips','Crisp battered white fish, oven chips, quick mushy peas and tartare sauce.',4,'55 min','Shared seafood meal · cod or haddock',
'cod:700; potato:1000; flour:180; cornflour:40; baking:1; oil:1000; peas:400; butter:20; lemon:1; mayo:100; caper:20; gherkin:40; malt:30; salt:1; blackpepper:0.5',[
'Heat the oven to 210°C fan. Cut potatoes into thick chips, boil for 5 minutes, drain and steam-dry. Toss with 30 ml of the oil and half the salt; roast for 35–40 minutes, turning halfway.',
'Mix mayonnaise with chopped capers, chopped gherkins and half the lemon juice. Cook peas according to their packet, drain, then mash with butter, pepper and 30 ml hot water.',
'Pat the fish dry and check for bones. Dust with 30 g of the flour. Mix the remaining 150 g flour, cornflour, baking powder and remaining salt. Whisk in 230 ml very cold water just before frying.',
'Heat the remaining oil in a deep, heavy pan to 175°C, never filling more than one third. Dip fish into batter and carefully lower into oil, cooking in batches for 6–9 minutes depending on thickness, until crisp and cooked through. Check the thickest part reaches 75°C for 30 seconds.',
'Drain on kitchen paper. Serve immediately with chips, peas, tartare, malt vinegar and the remaining lemon in wedges.' ],'Use a thermometer for the oil. The list includes a fresh batch of frying oil. For an oven-only version, buy breaded cod/haddock with no peanut ingredients, replace the fish-and-batter ingredients accordingly, and follow its packet.')
add('toad','uk','Friday','Dinner','Toad in the hole','Sausages in puffy batter, onion gravy, peas and carrots.',4,'55 min','3 pork + 1 vegetarian sausage portion',
'sausage:450; vegsausage:150; flour:160; egg:3; milk:250; oil:35; onion:300; stock:500; butter:20; soy:10; thyme:0.5; carrot:400; peas:300; salt:0.5; blackpepper:0.5',[
'Heat the oven to 210°C fan. Whisk 140 g flour, eggs, milk and salt into a smooth batter. Rest while the oven heats. Place pork sausages with 20 ml oil in a medium baking dish and vegetarian sausages with 10 ml oil in a small separate dish. Roast for 15 minutes.',
'Pour three quarters of the batter around the pork sausages and one quarter around the vegetarian sausages. Return to the oven for 25–30 minutes without opening the door, until puffed and golden and the pork sausages reach 75°C for 30 seconds.',
'For gravy, slice the onions and soften in butter and the remaining 5 ml oil for 15 minutes. Stir in the remaining 20 g flour, then gradually add stock, soy sauce, thyme and pepper. Simmer for 10 minutes.',
'Peel and slice carrots; steam or boil for 8–10 minutes. Cook peas according to the packet. Serve with both versions of the toad and shared vegetarian gravy.' ])
add('rarebit','uk','Saturday','Dinner','Welsh rarebit & tomato soup','Mustardy cheese toast, a little soup and a green salad.',3,'30 min','Meat-free for all 3',
'bread:300; cheddar:180; milk:80; mustard:15; soy:5; malt:5; butter:20; flour:15; tintomato:400; onion:100; stock:300; olive:15; salad:150; lemon:0.5; blackpepper:0.25; salt:0.25',[
'Chop onion and soften in 10 ml olive oil for 6 minutes. Add tomatoes, stock and salt; simmer for 15 minutes, then blend into a light soup.',
'Melt butter in a small saucepan and stir in flour for 1 minute. Gradually whisk in milk to make a thick paste. Remove from the heat and stir in grated cheddar, mustard, soy, malt vinegar and pepper.',
'Toast six slices of bread lightly on both sides. Spread with the cheese mixture and grill on a tray for 3–5 minutes until bubbling and browned; watch closely.',
'Dress salad leaves with the remaining 5 ml olive oil and lemon juice. Serve with rarebit and small bowls of soup.' ],'Soy sauce and malt vinegar provide the savoury tang here, avoiding a special bottle of Worcestershire sauce.')
add('cauliflower','uk','Sunday','Dinner','The cauliflower Sunday roast','Cauliflower cheese for three, roast potatoes, Yorkshires, vegetables and onion gravy.',3,'80 min','Meat-free for all 3',
'cauliflower:800; potato:750; carrot:300; peas:200; cheddar:180; milk:550; flour:145; butter:60; egg:2; oil:55; onion:200; stock:400; soy:10; mustard:10; thyme:0.5; salt:0.75; blackpepper:0.5',[
'Heat the oven to 200°C fan. Whisk 75 g flour, eggs, 150 ml milk and a quarter teaspoon salt into a batter; rest. Peel and cut potatoes, boil for 8 minutes, drain and roughen. Toss in 30 ml oil and roast for 50–60 minutes, turning halfway.',
'Cut cauliflower into florets and steam for 6–8 minutes until just tender; drain very well. Melt 40 g butter, stir in 40 g flour and cook for 1 minute. Whisk in the remaining 400 ml milk gradually. Simmer until thick, then stir in mustard, 140 g cheddar and half the pepper.',
'Put cauliflower in a roughly 20 cm baking dish, pour over sauce and top with the remaining cheese. Bake for 25 minutes until golden. Remove, cover loosely and keep warm while the Yorkshires bake. Potatoes may stay in the oven to finish crisping.',
'For gravy, soften sliced onions in the remaining 20 g butter for 15 minutes. Stir in the remaining 30 g flour, then stock, soy, thyme and remaining pepper and salt. Simmer for 10 minutes.',
'Raise oven to 210°C fan. Divide the remaining 25 ml oil among six metal muffin tin wells and heat for 5 minutes. Pour batter evenly into the hot wells and bake for 20–25 minutes without opening the door until risen and golden.',
'Steam sliced carrots for 8–10 minutes and cook peas according to their packet. Serve everything together, with two small Yorkshires each.' ])
add('full-english','uk','Saturday','Breakfast','A little Full English','A weekend breakfast for two meat-eaters and one meat-free diner.',3,'30 min','2 meat + 1 vegetarian breakfast',
'egg:3; sausage:200; bacon:100; vegsausage:100; bakedbeans:400; mushroom:250; tomato:300; bread:180; butter:20; oil:15; blackpepper:0.25',[
'Heat the oven to 190°C fan. Put pork sausages and bacon on one tray, vegetarian sausages on a separate small tray. Cook according to the packs, allowing about 20–25 minutes for raw pork sausages; check they reach 75°C for 30 seconds.',
'Halve tomatoes and slice mushrooms. Cook together in 10 ml oil in a separate pan for 8–10 minutes, seasoning with pepper. Warm baked beans in a saucepan.',
'Fry eggs in the remaining 5 ml oil until whites and yolks are set to your preference. Toast and butter the bread.',
'Build three plates: shared eggs, beans, mushrooms, tomatoes and toast, with pork and bacon on two plates and vegetarian sausages on one.' ])
add('toffee','uk','Saturday','Dessert','Sticky toffee pudding','A small date sponge with warm toffee sauce and ice cream.',3,'50 min','Meat-free · small bake for 3',
'date:90; bicarb:0.5; butter:60; brownsugar:100; egg:1; flour:90; baking:1; vanilla:0.5; cream:100; icecream:180',[
'Heat the oven to 170°C fan. Chop dates and pour over 120 ml boiling water. Stir in bicarbonate of soda and stand for 10 minutes; mash with a fork.',
'Beat 35 g softened butter with 40 g brown sugar. Beat in the egg and vanilla, then fold in flour, baking powder and the date mixture.',
'Line a small roughly 15 cm baking dish and add the batter. Bake for 25–30 minutes until a skewer inserted in the centre comes out clean.',
'For sauce, melt the remaining 25 g butter and 60 g sugar with the cream. Simmer for 3 minutes, stirring. Spoon over three portions of warm pudding and serve with ice cream.' ])
add('crumpets','uk','Sunday','Breakfast','Homemade crumpets','Small bubbly griddle cakes, butter and jam. No specialist bakery trip.',3,'35 min + 1 hr rising','Makes 6 · two each',
'flour:180; milk:150; yeast:1; sugar:5; salt:0.25; baking:0.5; oil:10; butter:30; jam:90',[
'Whisk flour, yeast, sugar and salt with the lukewarm milk and 150 ml lukewarm water. Cover for 1 hour until bubbly.',
'Stir baking powder into 15 ml water and beat into the batter. It should be thick but pourable; add a little more water if needed.',
'Lightly oil a non-stick frying pan and metal crumpet or egg rings. Heat on medium-low. Put rings in the pan and fill each about 1 cm deep. Cook for 8–10 minutes until holes appear and the top is almost set.',
'Remove rings carefully, turn and cook for 1–2 minutes. Repeat for six crumpets. Without rings, use smaller free-form rounds; they will be flatter and cook faster. Serve with butter and jam.' ])
add('crumble','uk','Sunday','Dessert','Apple crumble & custard','Tart apples under a buttery, golden crumble.',3,'45 min','Meat-free for all 3',
'apple:500; flour:90; butter:50; sugar:55; cinnamon:0.5; custard:300',[
'Heat the oven to 180°C fan. Core and slice apples. Put in a small baking dish with 20 g sugar, cinnamon and 30 ml water.',
'Rub cold cubed butter into flour until crumbly. Stir in the remaining 35 g sugar and scatter over the apples without pressing down.',
'Bake for 30–35 minutes until the fruit is soft and the topping golden. Rest for 5 minutes.',
'Warm custard according to the pack and pour over three portions of crumble.' ])
# K-store adaptations: regular rice vinegar, everyday soy, and mild miso.
CAT['vinegar']['label']='Rice vinegar'
CAT['soy']['label']='Soy sauce'
CAT['beanpaste']['label']='Vegan miso paste'
add('tomato-egg','china','Monday','Dinner','Tomato & egg','Soft eggs and juicy tomatoes, with rice and a cool cucumber salad.',4,'25 min','Meat-free for everyone',
'egg:8; tomato:800; spring:50; oil:30; sugar:10; salt:0.5; rice:300; cucumber:400; garlic:1; soy:15; vinegar:15; sesameoil:5',[
'Cook rice according to its packet. Cut cucumber into bite-size pieces and dress with crushed garlic, soy sauce, vinegar and sesame oil.',
'Beat eggs with half the salt. Heat 15 ml oil in a large frying pan and gently scramble the eggs until just set. Transfer to a plate.',
'Chop tomatoes and spring onions. Heat the remaining oil and cook tomatoes with sugar, remaining salt and 50 ml water for 5–8 minutes until juicy and partly broken down.',
'Fold the eggs and spring onions back in and heat through for 1 minute. Serve over rice with cucumber salad.' ])
add('mapo','china','Tuesday','Dinner','Mild mapo-style tofu','Mushrooms and tofu in a savoury sauce, with rice and garlicky greens.',4,'35 min','Meat-free for everyone',
'softtofu:600; mushroom:250; ginger:20; garlic:3; spring:50; beanpaste:30; soy:20; stock:300; cornflour:15; oil:25; rice:300; pakchoi:400; chilli:2; blackpepper:0.25',[
'Cook rice according to its packet. Cut tofu into 2 cm cubes. Finely chop mushrooms, ginger, garlic and spring onions.',
'Heat 15 ml oil in a wide pan and fry mushrooms for 7 minutes until browned. Add ginger, two thirds of the garlic and the white spring onion parts; stir for 1 minute.',
'Mix miso with the stock and soy sauce; pour into the pan. Add tofu and simmer gently for 6–8 minutes. Mix cornflour with 30 ml cold water, fold into the sauce and simmer for 2 minutes until lightly thickened. Add black pepper and green spring onion tops.',
'In another pan, heat the remaining 10 ml oil with the remaining garlic. Add chopped pak choi and 30 ml water, cover for 2 minutes, then stir-fry uncovered for 2 minutes. Serve with rice; put chilli flakes on the table.' ],'This is a mild K-store adaptation using vegan miso instead of doubanjiang. It does not reproduce the heat or flavour of traditional Sichuan mapo tofu. Firm tofu also works if soft tofu is unavailable.')
add('char-siu','china','Wednesday','Dinner','Char siu-style pork & tofu','Sticky oven-roasted pork and a separate tofu portion, with pak choi and rice.',4,'65 min + 30 min marinating','3 pork + 1 tofu',
'pork:600; tofu:200; hoisin:60; soy:30; honey:30; cinnamon:0.25; blackpepper:0.25; garlic:3; ginger:15; oil:20; rice:300; pakchoi:500',[
'Cut pork into long strips about 3 cm thick and tofu into thick slabs. Mix hoisin, soy, honey, cinnamon, black pepper, grated ginger and two crushed garlic cloves. Reserve one quarter in a clean bowl for tofu. Marinate pork and tofu separately in their sauce for at least 30 minutes in the fridge.',
'Heat the oven to 190°C fan. Put pork and its marinade in a lined roasting dish; put tofu and its marinade in another small dish. Roast pork for 35–45 minutes, turning halfway, until the centre reaches 75°C for 30 seconds. Roast tofu for 25–30 minutes. Add a splash of water if the glaze begins to catch.',
'Cook rice according to the packet. Slice pak choi, heat oil in a pan and fry the remaining chopped garlic for 30 seconds. Add greens and 40 ml water; cover for 2 minutes, then uncover and stir-fry for 2–3 minutes.',
'Rest pork for 5 minutes, slice and serve with rice and greens; serve tofu separately. Do not use uncooked marinade as a finishing sauce.' ],'The hoisin product must have no peanut ingredients; “may contain” is acceptable for this household.')
add('chow-mein','china','Thursday','Dinner','Chicken & vegetable chow mein','A colourful noodle dinner with an easy tofu portion.',4,'30 min','3 chicken + 1 tofu',
'chicken:450; tofu:150; noodles:300; carrot:200; cabbage:300; pepper:200; spring:50; garlic:3; ginger:15; soy:45; hoisin:30; sesameoil:10; oil:30',[
'Cook noodles according to their packet, drain and toss with sesame oil. Thinly slice chicken, cube tofu and cut vegetables into thin strips. Mix soy sauce, hoisin and 50 ml water in a bowl.',
'Stir-fry chicken in 10 ml oil for 7–10 minutes, until cooked through at 75°C for 30 seconds. Set aside. In a separate small pan, brown tofu in 5 ml oil for 6–8 minutes.',
'In a clean large wok or pan, heat the remaining 15 ml oil. Fry chopped garlic and ginger for 30 seconds, add carrots, cabbage and pepper, and stir-fry for 5 minutes.',
'Add noodles, sauce and spring onions; toss until hot. Move one quarter of the noodle mixture to the tofu pan. Add chicken to the larger portion. Heat both through and serve.' ])
add('jiaozi','china','Friday','Dinner','Jiaozi dumpling night','Make, fold and share: pork-and-cabbage and mushroom dumplings.',4,'90 min','24 pork + 8 mushroom dumplings',
'flour:380; porkmince:300; mushroom:150; cabbage:300; spring:50; ginger:20; garlic:2; soy:60; vinegar:40; sesameoil:15; oil:30; cucumber:400; salt:0.75',[
'Mix 360 g flour with half a teaspoon salt and 190 ml warm water, adding water a spoonful at a time if needed to form a firm dough. Knead for 8 minutes and cover to rest for 30 minutes. Reserve 20 g flour for rolling.',
'Finely chop cabbage, mix with the remaining salt, rest 10 minutes and squeeze dry. Finely chop spring onion, ginger and one garlic clove. Divide these vegetables 3:1 between two bowls. Add pork, 15 ml soy and 5 ml sesame oil to the larger bowl.',
'Finely chop mushrooms and fry in 5 ml rapeseed oil until dry; cool. Add to the smaller vegetable bowl with 5 ml soy and 5 ml sesame oil. Keep filling bowls and utensils separate.',
'Divide dough into 32 pieces. Roll into thin 10–11 cm circles on the reserved flour. Fill 24 with pork mixture and 8 with mushroom mixture, dividing each filling evenly among its wrappers (about a heaped tablespoon each); pinch tightly shut. Use a different fold for the mushroom batch.',
'Cook batches in separate non-stick pans. Use the remaining 25 ml rapeseed oil across the batches. Fry bases for 2 minutes, add water to 5 mm deep and cover. Steam for 8–10 minutes; check pork filling reaches 75°C for 30 seconds. Uncover and let water evaporate to crisp the bases.',
'Mix 30 ml soy and 30 ml vinegar with 20 ml water as dipping sauce. Smash and chop cucumber; dress with the remaining 10 ml soy, 10 ml vinegar, 5 ml sesame oil and crushed garlic clove. Serve alongside.' ],'Homemade wrappers avoid relying on frozen dumpling skins. Fold the mushroom batch first. A wide frying pan with a well-fitting lid is sufficient.')
add('gong-bao','china','Saturday','Dinner','Gong bao-style chicken','A tangy, glossy stir-fry with peppers; no peanuts added.',4,'35 min','3 chicken + 1 tofu',
'chicken:450; tofu:150; pepper:300; carrot:200; spring:75; ginger:20; garlic:3; soy:40; vinegar:30; sugar:20; cornflour:20; oil:30; rice:300; chilli:2',[
'Cook rice according to the packet. Cube chicken and tofu. Mix soy, vinegar, sugar, cornflour and 120 ml water. Reserve one quarter of this clean sauce for the tofu pan.',
'Brown tofu in 5 ml oil in a small pan for 6–8 minutes. In a larger pan, stir-fry chicken in 10 ml oil for 7–10 minutes, until it reaches 75°C for 30 seconds. Set each aside in separate bowls.',
'Chop peppers and carrots into small pieces. Stir-fry in the remaining 15 ml oil for 5 minutes in a clean pan. Add chopped ginger, garlic and spring onion and fry for 1 minute.',
'Divide vegetables 3:1 between the chicken and tofu pans. Stir each reserved sauce before adding. Simmer each for 2–3 minutes until glossy and hot throughout. Serve with rice and chilli flakes separately.' ],'A family adaptation of gong bao: the peanuts are omitted, with no nut replacement needed.')
add('hot-pot','china','Sunday','Dinner','The big family hot pot','A bubbling vegetable broth, a colourful spread and a little beef pot on the side.',4,'45 min + cooking at the table','Shared meat-free pot + beef for 3',
'stock:2500; ginger:40; garlic:4; spring:100; mushroom:500; pakchoi:400; cabbage:400; carrot:200; tofu:600; hotbeef:450; noodles:250; soy:80; vinegar:50; sesameoil:20; sesame:20; chilli:2',[
'You need two pots, separate ladles and tongs, and a safe tabletop cooker; alternatively keep both pots simmering on the hob and serve cooked batches at the table. Keep raw-meat plates and utensils separate from cooked food.',
'Simmer stock with sliced ginger, two crushed garlic cloves and half the spring onions for 15 minutes. Transfer 750 ml broth to the separate meat pot; keep 1.75 litres in the shared pot. Bring both to a steady simmer.',
'Slice mushrooms, wash and chop pak choi and cabbage, cut carrots very thinly and cube tofu. Arrange on platters. Keep the thinly sliced raw beef refrigerated until cooking. Cook noodles separately according to the packet and divide into bowls.',
'Mix soy, vinegar and sesame oil with 50 ml water. Add the remaining finely chopped garlic and spring onions. Divide among dipping bowls and offer sesame seeds and chilli separately.',
'Add small batches of mushrooms and carrots to the shared pot; simmer for 4–6 minutes, then add greens and tofu for 3–5 minutes, until hot and tender. Cook beef only in its separate pot in small batches until fully cooked; check a folded thick piece reaches 75°C for 30 seconds. Do not treat a brief dip as sufficient.',
'Serve cooked food with noodles and dipping sauces, adding hot water to the pots as the broth reduces. Keep both pots simmering throughout service. Use clean eating utensils, not the raw-meat tongs.' ],'Amounts include beef for three and tofu to share with all four. This is a mild, supermarket-friendly hot pot; everyone can season their own dipping bowl.')
add('congee','china','Saturday','Breakfast','Breakfast congee','A gentle rice porridge with eggs, spring onion and crisp onion topping.',4,'65 min','Meat-free for everyone',
'rice:180; egg:4; ginger:15; spring:50; onion:100; oil:20; soy:20; sesameoil:5; salt:0.25',[
'Rinse rice, then put in a large saucepan with 1.5 litres water, sliced ginger and salt. Bring to a boil, reduce heat and simmer partly covered for 50–60 minutes, stirring occasionally, until creamy. Add hot water if too thick.',
'Boil eggs for 9–10 minutes, cool under cold water, peel and halve. Thinly slice onion and fry in rapeseed oil for 10–15 minutes until golden; drain on kitchen paper.',
'Remove ginger slices from the porridge. Divide between four bowls and top with eggs, crisp onions and chopped spring onions.',
'Mix soy and sesame oil and let everyone add a little to their bowl.' ])
add('mango-pudding','china','Saturday','Dessert','Mango pudding','Sunny mango-and-coconut cups, set without gelatine.',4,'20 min + 3 hr chilling','Meat-free for everyone',
'mango:300; coconut:250; sugar:30; agar:2.5',[
'Blend thawed mango flesh until smooth and let it reach room temperature. You need about 300 ml purée.',
'Whisk agar powder and sugar into coconut milk in a saucepan. Bring to a boil while stirring, then simmer for 2 minutes to dissolve the agar; follow the product’s activation instructions if they differ.',
'Quickly whisk in the mango purée over low heat until smooth and steaming. Do not let it cool in the pan. Divide among four small glasses.',
'Cool, then refrigerate for at least 3 hours until set. Serve chilled in the glasses.' ],'Use pure agar powder, not a sweetened gelling mixture. Strength varies by brand; follow the pack dosage for roughly 550 ml mixture if different. K-Ruoka lists Meira agar agar.')
add('scallion-pancakes','china','Sunday','Lunch','Scallion pancakes','Flaky, savoury pancakes with a tangy dipping sauce.',4,'50 min','4 pancakes · light lunch',
'flour:320; spring:100; oil:55; salt:0.5; soy:30; vinegar:20; sesameoil:5',[
'Mix 300 g flour with salt. Carefully stir in 180 ml freshly boiled water. When cool enough to handle, knead for 5 minutes until smooth; cover and rest for 20 minutes. Reserve 20 g flour for rolling.',
'Divide into four. Roll each into a thin rectangle, brush with some of 25 ml oil and scatter with chopped spring onions. Roll into a log, coil into a spiral and flatten gently. Rest for 5 minutes, then roll into 16–18 cm discs.',
'Use the remaining 30 ml oil to pan-fry the pancakes over medium heat for 3–4 minutes per side, until golden and cooked inside. Press lightly with a spatula as they cook.',
'Mix soy, vinegar, sesame oil and 20 ml water. Cut pancakes into wedges and serve with the dipping sauce.' ])
add('sesame-biscuits','china','Sunday','Dessert','Sesame biscuits & ice cream','A simple sesame-scented finale using everyday baking ingredients.',4,'30 min','Makes about 12 biscuits · replaces sesame balls',
'flour:120; butter:70; sugar:50; sesame:40; milk:20; baking:0.5; icecream:300',[
'Heat the oven to 170°C fan. Beat softened butter and sugar until creamy. Mix flour with baking powder and 25 g sesame seeds, then stir into the butter with the milk to make a soft dough.',
'Divide into twelve balls and flatten on a lined tray, leaving space between them. Press the remaining 15 g sesame seeds onto the tops.',
'Bake for 14–18 minutes until the edges are pale gold. Leave on the tray for 5 minutes, then cool on a rack.',
'Serve three biscuits each with vanilla ice cream.' ],'An easy family substitution for sesame balls, not a traditional version of that dish. Sesame remains an ingredient; only peanuts are excluded.')
# The Greek bakes use the same easily found cheddar as UK week.
for recipe in RECIPES:
    for item in recipe['ingredients']:
        if item['key']=='hardcheese': item['key']='cheddar'
