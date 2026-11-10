# API lab

Individual homework for ITDS362. These tests use the QuickPizza demo API at `https://quickpizza.grafana.com`.

## Install and run

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -v
pytest -v --html=report.html --self-contained-html
```

Each test creates a uniquely named practice user when it needs authenticated data. The shared practice token is used only by the read-only tools check. Tests create ratings only under their own user and clean up the rating fixture after each test. A full run sends many requests to the public demo; run it once when preparing the report, not in a loop.

## Input domain model: POST /api/ratings

The request has `pizza_id` and `stars` fields and requires the logged-in user's token.

| Characteristic | Blocks | Example / covering test |
|---|---|---|
| C1: star value | below 1; 1–5 (base); above 5 | 0 or 6: `test_stars_out_of_range`; 3: `test_base_choice_is_saved` |
| C2: star type | whole number (base); decimal; text; missing | `test_base_choice_is_saved`; `test_decimal_stars_are_refused`; `test_text_stars_are_refused`; `test_missing_stars_are_refused` |
| C3: pizza | exists (base); does not exist | `test_base_choice_is_saved`; `test_unknown_pizza_is_refused` |
| C4: token | user's own (base); none; invalid short token | `test_base_choice_is_saved`; `test_missing_token_is_refused`; `test_short_token_is_refused` |

Base choice uses four tests: the base case plus one test for each of the other C1/C2/C3/C4 blocks (2 + 3 + 1 + 2). All combinations would require 3 × 4 × 2 × 3 = 72 tests.
