#!/usr/bin/env python3
"""Loan amortization schedule generator.

Builds a month-by-month amortization schedule for a fixed-rate loan:
monthly payment, interest/principal split, remaining balance, total
interest, and a year-by-year summary. Standard library only.

Example:
    python3 loan_amortization.py --principal 25000 --rate 6.5 --years 5
"""

import argparse


def monthly_payment(principal: float, annual_rate_pct: float, years: int) -> float:
    """Fixed monthly payment for an amortizing loan."""
    r = annual_rate_pct / 100 / 12
    n = years * 12
    if r == 0:
        return principal / n
    return principal * r / (1 - (1 + r) ** -n)


def build_schedule(principal: float, annual_rate_pct: float, years: int):
    """Return (rows, total_interest). Each row is a dict for one month."""
    r = annual_rate_pct / 100 / 12
    payment = monthly_payment(principal, annual_rate_pct, years)
    balance = principal
    rows = []
    total_interest = 0.0
    for month in range(1, years * 12 + 1):
        interest = balance * r
        principal_paid = payment - interest
        # Final month: clear whatever balance remains (rounding).
        if month == years * 12:
            principal_paid = balance
        balance -= principal_paid
        total_interest += interest
        rows.append(
            {
                "month": month,
                "payment": payment if month < years * 12 else principal_paid + interest,
                "interest": interest,
                "principal": principal_paid,
                "balance": max(balance, 0.0),
            }
        )
    return rows, total_interest


def main() -> None:
    parser = argparse.ArgumentParser(description="Loan amortization schedule")
    parser.add_argument("--principal", type=float, default=25000, help="Loan amount ($)")
    parser.add_argument("--rate", type=float, default=6.5, help="Annual interest rate (%%)")
    parser.add_argument("--years", type=int, default=5, help="Term in years")
    args = parser.parse_args()

    rows, total_interest = build_schedule(args.principal, args.rate, args.years)
    payment = monthly_payment(args.principal, args.rate, args.years)

    print(f"Loan: ${args.principal:,.2f} at {args.rate}% for {args.years} years")
    print(f"Monthly payment: ${payment:,.2f}\n")

    print(f"{'Month':>5}  {'Payment':>9}  {'Interest':>9}  {'Principal':>9}  {'Balance':>11}")
    for row in rows[:6]:
        print(
            f"{row['month']:>5}  {row['payment']:>9,.2f}  {row['interest']:>9,.2f}  "
            f"{row['principal']:>9,.2f}  {row['balance']:>11,.2f}"
        )
    print("  ...")

    print("\nYear-end balances:")
    for year in range(1, args.years + 1):
        row = rows[year * 12 - 1]
        year_interest = sum(r["interest"] for r in rows[(year - 1) * 12 : year * 12])
        print(
            f"  Year {year}: balance ${row['balance']:,.2f}, "
            f"interest paid ${year_interest:,.2f}"
        )

    print(f"\nTotal interest over {args.years} years: ${total_interest:,.2f}")
    print(f"Total cost of the loan: ${args.principal + total_interest:,.2f}")


if __name__ == "__main__":
    main()
