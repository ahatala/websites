"""Validate the agreed schedule, portions, ingredient totals and local links."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
from collections import defaultdict
ROOT=Path(__file__).parent
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__();self.ids=set();self.links=[];self.ingredients=[];self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:
            assert a['id'] not in self.ids,('duplicate id',a['id'])
            self.ids.add(a['id'])
        for key in ('href','src'):
            if key in a:self.links.append(a[key])
pages={p:Page(p.read_text()) for p in ROOT.rglob('*.html')}
for path,page in pages.items():
    for link in page.links:
        url=urlsplit(link)
        if url.scheme or url.netloc:continue
        target=(path.parent/unquote(url.path)).resolve() if url.path else path
        assert target.exists(),(path,link)
        if url.fragment:assert target in pages and unquote(url.fragment) in pages[target].ids,(path,link)
data=json.loads((ROOT/'assets/menu.json').read_text());recipes=data['recipes']
expected={
'greece':{'Monday':'souvlaki','Tuesday':'spanakopita','Wednesday':'fasolada','Thursday':'giouvetsi','Friday':'saganaki','Sunday':'moussaka'},
'uk':{'Monday':'tikka','Tuesday':'cottage','Wednesday':'leek-soup','Thursday':'fish-chips','Friday':'toad','Saturday':'rarebit','Sunday':'cauliflower'},
'china':{'Monday':'tomato-egg','Tuesday':'mapo','Wednesday':'char-siu','Thursday':'chow-mein','Friday':'jiaozi','Saturday':'gong-bao','Sunday':'hot-pot'}}
for week,days in expected.items():
    actual={r['day']:r['id'] for r in recipes if r['week']==week and r['kind']=='Dinner'}
    assert actual==days,(week,actual)
    totals=defaultdict(float)
    for r in recipes:
        if r['week']!=week:continue
        expected_servings=3 if (week=='greece' and r['day']=='Thursday') or (week=='uk' and r['day'] in ('Saturday','Sunday')) else 4
        assert r['servings']==expected_servings,r['id']
        assert r['steps'] and len(r['ingredients'])>=4
        for i in r['ingredients']:
            assert i['qty']>0
            assert i['key'] in data['ingredients']
            totals[i['key']]+=i['qty']
    assert dict(totals)==data['shopping'][week]
    shop=pages[ROOT/f'{week}-shopping.html']
    assert {i.removeprefix('shop-') for i in shop.ids if i.startswith('shop-')}==set(totals)
assert not any(r['week']=='greece' and r['day']=='Saturday' for r in recipes)
by_id={r['id']:r for r in recipes}
assert 'sesame-biscuits' in by_id and 'sesame-balls' not in by_id
meat={'chicken','beef','mince','pork','porkmince','hotbeef','sausage','bacon'}
for name in ['cottage','leek-soup','cauliflower','rarebit','fasolada','spanakopita','mapo']:
    assert not meat.intersection(i['key'] for i in by_id[name]['ingredients']),name
assert not {'mushroom','tofu'}.intersection(i['key'] for i in by_id['giouvetsi']['ingredients'])
assert all('peanut' not in i['key'] and 'salmon' not in i['key'] for r in recipes for i in r['ingredients'])
assert len(recipes)==30
print(f'PASS: {len(pages)} pages; all local links and anchors; 30 recipes; agreed schedule, portions and all shopping totals.')
