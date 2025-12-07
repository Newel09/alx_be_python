import os
import sys

# Ensure imports work when running this file directly
sys.path.insert(0, os.path.dirname(__file__))

import budget
import shopping_manager


def main():
    income = budget.get_monthly_income()
    allocations = budget.get_allocations()
    amounts = budget.compute_amounts(income, allocations)

    print("\nBudget breakdown:")
    print(f"- Investment (long-term) ({allocations.get('investment',0):.2f}%): ${amounts['investment']:,.2f}")
    print(f"- Savings (short-term) ({allocations.get('savings',0):.2f}%): ${amounts['savings']:,.2f}")
    print(f"- Groceries ({allocations.get('groceries',0):.2f}%) - shopping budget: ${amounts['groceries']:,.2f}")
    print(f"- Transportation ({allocations.get('transportation',0):.2f}%): ${amounts['transportation']:,.2f}")
    print(f"- Tithe ({allocations.get('tithe',0):.2f}%): ${amounts['tithe']:,.2f}\n")

    shopping_manager.run_shopping_manager(amounts['groceries'])


if __name__ == "__main__":
    main()
