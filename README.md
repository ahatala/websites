# Family Food Festival

A static family menu, recipe collection and weekly shopping planner.

Live site: https://ahatala.github.io/websites/

## Content

- Greece: six dinners, Thursday for three, no Saturday meals, moussaka on Sunday.
- United Kingdom: four weekday diners, three weekend diners; cauliflower Sunday roast for everyone.
- China: four diners; separate meat-free portions where needed, Sunday hot pot and sesame biscuits.
- No peanut ingredients, peanut oil or salmon/red-fleshed fish. “May contain peanuts” is acceptable for this household. Other allergens are not excluded.
- K-Citymarket Helsinki Ruoholahti is the shopping reference. Product examples were checked in K-Ruoka's catalogue on 2026-09-11; live store stock was not verified. Links do not add anything to a cart.

There are 30 recipe pages, three country pages, three shopping pages and a home page. All content is available without JavaScript. JavaScript adds printable-page buttons, copy fallback, saved shopping ticks and the family scorecard. Browser-local data is not synchronized.

## Editing

1. Edit recipes and ingredient quantities in `menu.py`.
2. Edit Finnish ingredient names, product examples and pack guidance in `shopping.py`.
3. Edit templates in `build.py`, styles in `assets/style.css` and behavior in `assets/app.js`.
4. Run `python3 build.py`, then `python3 validate.py`.
5. Commit both source and regenerated HTML, JSON and text lists. GitHub Pages serves `main` at `/`.

`build.py` uses only the Python standard library. Shopping totals are generated from exactly the same quantities used on recipe pages; packs are rounded separately. Optional swaps described in notes are not automatically substituted into shopping totals.

`illustrations.py` produces the four original SVG food illustrations; rerun it after editing those drawings. No external fonts, trackers, analytics or image services are required by the site.

## Preview

Run `python3 -m http.server 8765 --bind 127.0.0.1` and open http://127.0.0.1:8765/.

`validate.py` checks local links and anchors, the agreed dinner schedule, attendance, key dietary choices and shopping-list coverage/totals. Browser checks additionally covered all pages at desktop and phone widths, checklist persistence and isolation, scorecard persistence, copy/download and print layouts.

Recipes are written as family adaptations, not represented as professionally kitchen-tested recipes. The hot-pot recipe links to a setup reference; cooking-temperature guidance links to GOV.UK. The K-Ruoka product links are shopping references, not recipe attribution or a guarantee of availability or allergen suitability.
