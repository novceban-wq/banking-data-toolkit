# Banking Data Toolkit

Small, practical Python tools for Canadian banking data analysis and automation.
Built as a learning/portfolio project: each script solves one real banking task,
runs from the command line, and explains its own output.

## What's inside

| Script | What it does | Dependencies |
| --- | --- | --- |
| `loan_amortization.py` | Builds a full amortization schedule for a fixed-rate loan — monthly payment, interest/principal split, remaining balance, total interest, plus a year-by-year summary. | None (standard library only) |
| `bank_stock_compare.py` | Pulls live data for the Big Six Canadian banks (TD, RY, BMO, BNS, CM, NA on the TSX) and prints a comparison table: price, dividend yield, P/E ratio, market cap. | `yfinance`, `pandas` |

## Quick start

```bash
# No dependencies needed for the loan tool
python3 loan_amortization.py --principal 25000 --rate 6.5 --years 5

# For the stock comparison tool
pip install -r requirements.txt
python3 bank_stock_compare.py
```

Example output (loan tool, first rows):

```text
Month   Payment  Interest  Principal   Balance
    1    489.15    135.42     353.74  24,646.26
    2    489.15    133.50     355.65  24,290.61
  ...
Total interest over 5 years: $4,349.22
```

## Roadmap

- [ ] Export schedules to CSV/Excel for client-ready worksheets
- [ ] Add a debt-service coverage (DSCR) calculator for small-business lending
- [ ] Pull Bank of Canada policy-rate history and chart it against loan pricing
- [ ] Turn the stock comparison into a scheduled weekly email summary

## About

Built by Johnny Chen — MBA candidate at Vancouver Island University with a
background in front-line banking (TD Canada Trust) and account management.
Interested in Canadian banking, relationship management, and using data
automation to spend less time on spreadsheets and more time with clients.

*Turning conversations into trusted relationships.*
