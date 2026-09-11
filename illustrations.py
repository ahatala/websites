from pathlib import Path
from math import sin, cos, pi

def save(name, body):
    Path(f'assets/{name}.svg').write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 440" fill="none"><g stroke="#294f40" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{body}</g></svg>''')
# Original, code-drawn food illustrations; no external assets.
plate='<ellipse cx="250" cy="280" rx="197" ry="125" fill="#d6d4ae" stroke="none"/><ellipse cx="250" cy="264" rx="198" ry="128" fill="#fffdf3"/><ellipse cx="250" cy="262" rx="170" ry="104" stroke="#718d9c"/><ellipse cx="250" cy="262" rx="160" ry="96" stroke="#718d9c"/>'
greek=plate
for x,y in [(153,245),(245,208),(330,255),(260,300),(178,308)]:
    greek+=f'<path d="M{x-25} {y}q20-42 48-8q19 31-14 44q-35 10-34-36Z" fill="#d95c3a"/><path d="M{x-8} {y-5}l8 13m11-14l-4 17" stroke="#f6b86a"/>'
for x,y in [(203,253),(286,252),(222,323),(341,292),(135,278)]:
    greek+=f'<ellipse cx="{x}" cy="{y}" rx="23" ry="16" fill="#8baf64"/><ellipse cx="{x}" cy="{y}" rx="14" ry="9" fill="#dbe5a1" stroke-width="1"/>'
for x,y in [(213,203),(286,283),(160,285)]:
    greek+=f'<path d="M{x} {y}l48-9 12 31-50 13Z" fill="#fff8d9"/><path d="M{x+8} {y+8}l5-1m19 7 6-1" stroke="#c4b990"/>'
for x,y in [(245,252),(185,222),(317,304),(311,213)]:
    greek+=f'<ellipse cx="{x}" cy="{y}" rx="10" ry="7" fill="#3b4b35"/>'
greek+='''<path d="M327 133c-7-49 28-70 61-43 28 24 12 66-31 69Z" fill="#e9b93e"/><path d="m349 108 20 38m-34-20 45-14" stroke="#fff2ac"/><path d="M365 79q-7-42 29-36-1 28-29 36Z" fill="#668751"/><path d="M94 169q-2-68-35-91m16 28q-44-11-32-35 29 5 32 35Zm13 31q-34-7-29-28 22 3 29 28Zm-11-30q35-29 37-6-8 20-37 6Z" fill="#7a9b63"/><path d="M390 330q26-45 49-49m-32 27q26 15 33-6-20-10-33 6Zm17-17q-16-22 3-29 14 11-3 29Z" fill="#779760"/><path d="m131 100 12-15m-1 30 18-3m-38-33 1-16" stroke="#b97538"/>'''
save('greece',greek)
uk='''<ellipse cx="244" cy="322" rx="194" ry="72" fill="#d7c3a1" stroke="none"/><path d="M73 228h324l-23 103q-6 30-49 33H135q-41-4-47-33Z" fill="#7b9686"/><path d="M80 249h309m-291 64h274" stroke="#d8e1ba"/><path d="M72 248q-51-5-38 28 5 14 46 13m318-41q51-5 38 28-5 14-45 13" stroke-width="9"/><ellipse cx="235" cy="224" rx="168" ry="66" fill="#f1c36a"/><ellipse cx="235" cy="224" rx="156" ry="55" fill="#efd698" stroke="#be7e3b"/>'''
for x,y,r in [(136,220,23),(187,201,27),(241,206,27),(299,212,26),(337,232,20),(274,242,27),(208,241,23),(161,248,19)]:
    uk+=f'<path d="M{x-r} {y}q-5-16 12-18 3-18 20-11 20-4 22 14 14 14-1 25-12 12-30 6-24 7-23-16Z" fill="#fff0b8" stroke="#b78c45"/><path d="m{x-4} {y-10}8 6m-11 9 14-1" stroke="#d99442"/>'
uk+='''<path d="M167 126q-20-24 0-45t-2-42m62 87q-20-24 0-45t-2-42m62 87q-20-24 0-45t-2-42" stroke="#bd8c65" stroke-width="4"/><path d="M360 111h70v60q-3 27-35 27t-35-27Z" fill="#fcf4de"/><path d="M430 127q37-3 25 28-7 16-25 11" stroke-width="7"/><ellipse cx="395" cy="111" rx="35" ry="10" fill="#b66f3e"/><path d="m123 359-14 40 56-18m159-2 50 22-7-50" fill="#d9954b"/><path d="m100 158-16-12m31-3-5-18m225 233 13 11" stroke="#b97538"/>'''
save('uk',uk)
china='''<ellipse cx="250" cy="331" rx="196" ry="68" fill="#dbb99e" stroke="none"/><path d="M97 223h303l-19 108q-9 40-133 40T116 331Z" fill="#b84f3b"/><path d="M121 321q128 37 261 0" stroke="#e99564"/><path d="M94 247q-53-1-43 29 6 17 51 15m300-44q50 0 39 29-5 17-49 15" stroke-width="10"/><ellipse cx="248" cy="226" rx="155" ry="66" fill="#e6b760"/><ellipse cx="248" cy="226" rx="140" ry="54" fill="#ac7342"/>'''
for x,y in [(165,211),(236,250),(311,224)]:
    china+=f'<path d="M{x-26} {y+8}q23-66 56-5-19 22-56 5Z" fill="#fff0c5"/><path d="m{x-5} {y-14}-4 20m16-21 4 19m8-7 6 12" stroke="#b18b55" stroke-width="2"/>'
for x,y in [(204,204),(302,252),(337,209)]:
    china+=f'<path d="M{x} {y}q-30-29-2-40 22 5 14 29 34-31 40-8-11 28-41 24Z" fill="#70945b"/><path d="m{x+9} {y+10}5-23" stroke="#d3e6a2"/>'
china+='''<path d="m168 90 176 112m-157-130 160 120" stroke="#70462e" stroke-width="7"/><path d="M270 139q-19-21-3-39t-4-35m66 90q-19-21-3-39t-4-35" stroke="#ba8c66" stroke-width="4"/><path d="M58 151q33-10 64 1l-7 35q-25 21-50-1Z" fill="#fff2d1"/><ellipse cx="90" cy="152" rx="32" ry="9" fill="#734b2f"/><path d="M169 382q12-16 24-7m-5 10 17-5m154-235 15-13m-4 28 20-3" stroke="#b57543"/>'''
save('china',china)
# A three-country table for the landing page.
save('table','''<path d="M42 116h416v264H42Z" fill="#e8c8a1" stroke="none"/><path d="M42 162h416M42 217h416M42 272h416M42 327h416M96 116v264m58-264v264m58-264v264m58-264v264m58-264v264m58-264v264m58-264v264" stroke="#fff3d4" stroke-width="15"/><ellipse cx="174" cy="213" rx="106" ry="83" fill="#fffdf4"/><ellipse cx="174" cy="213" rx="87" ry="66" stroke="#6e8b94"/><path d="M123 191q30-50 54 3-29 34-54-3Z" fill="#d66540"/><path d="M171 219q30-50 54 3-29 34-54-3Z" fill="#d66540"/><ellipse cx="138" cy="236" rx="23" ry="17" fill="#86a768"/><ellipse cx="201" cy="184" rx="23" ry="17" fill="#86a768"/><path d="m154 184 41 10-10 29-41-10Z" fill="#fff1c7"/><path d="M280 199h145l-12 87q-6 20-59 20t-61-20Z" fill="#be593e"/><ellipse cx="351" cy="198" rx="75" ry="35" fill="#e9c276"/><path d="M305 201q26-56 54-3-24 24-54 3Zm53 4q26-56 54-3-24 24-54 3Z" fill="#fff0c6"/><path d="m322 181 4 20m17-22-3 18m39-20 4 20m17-22-3 18" stroke="#bc9763"/><path d="m330 144-22-65m38 60-15-62" stroke="#775437" stroke-width="6"/><path d="M218 311h65v39q0 20-32 20t-33-20Z" fill="#fff7e7"/><ellipse cx="251" cy="311" rx="33" ry="10" fill="#a77347"/><path d="M283 320q28 0 17 19-4 10-17 8" stroke-width="6"/><path d="m221 78 18-23m11 37 27-11m-78 17-2-23" stroke="#b17639"/><path d="M94 326q-4-36-33-42m20 32q30-22 36-1-9 17-36 1Z" fill="#7d985a"/><path d="M389 350q-12-37 20-45 41 11 9 46Z" fill="#eab940"/>''')
