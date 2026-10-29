#!/usr/bin/env python3
"""Compare the Big Six Canadian banks listed on the TSX.

Fetches current price, dividend yield, P/E ratio and market cap for
TD, RY (RBC), BMO, BNS (Scotiabank), CM (CIBC) and NA (National Bank)
using Yahoo Finance data via yfinance, and prints a comparison table.

Setup:
    pip install -r requirements.txt
Run:
    python3 bank_stock_compare.py
"""

TICKERS = {
    "TD.TO": "TD Bank",
    "RY.TO": "RBC",
    "BMO.TO": "BMO",
    "BNS.TO": "Scotiabank",
    "CM.TO": "CIBC",
    "NA.TO": "National Bank",
}


def main() -> None:
    try:
        import yfinance as yf
    except ImportError:
        print("yfinance is not installed. Run: pip install -r requirements.txt")
        return

    rows = []
    for symbol, name in TICKERS.items():
        info = yf.Ticker(symbol).info
        rows.append(
            {
                "Bank": name,
                "Price": info.get("currentPrice") or info.get("regularMarketPrice"),
                "Div yield %": (info.get("dividendYield") or 0) * 100,
                "P/E": info.get("trailingPE"),
                "Market cap ($B)": (info.get("marketCap") or 0) / 1e9,
            }
        )

    try:
        import pandas as pd

        df = pd.DataFrame(rows).sort_values("Market cap ($B)", ascending=False)
        print(df.to_string(index=False, float_format=lambda x: f"{x:,.2f}"))
    except ImportError:
        for row in rows:
            print(row)


if __name__ == "__main__":
    main()
