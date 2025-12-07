# Capstone Project — Shopping & Budget Manager

This small capstone demonstrates a simple CLI application to help a user allocate a monthly income across common categories and manage a groceries shopping list.

Core goals:
- Teach modular Python organization (separate modules for budget and shopping manager).
- Provide an interactive, user-friendly CLI for allocating budget percentages and building a shopping list.
- Make future enhancements easy (price tracking, persistence, tests).

What it includes
- `main.py` — entrypoint: prompts for income and percentage allocations, prints the computed budget breakdown, then launches the shopping manager.
- `budget.py` — helpers for `get_monthly_income()`, `get_allocations()`, and `compute_amounts(income, allocations)`.
- `shopping_manager.py` — shopping menu and `run_shopping_manager(groceries_budget)` (add/remove/view/exit).
- `shopping_list_manager.py` — small backward-compatible wrapper that calls `main()`.

How it works (quick)
1. Run the program.
2. Enter your monthly income when prompted.
3. Allocate percentages for: Investment (long-term), Savings (short-term), Groceries, Transportation, and Tithe. The allocations must total 100%.
4. The program prints each category's percentage and the calculated monetary amount.
5. The shopping manager starts and shows your groceries budget; you can add, remove, or view items.

Run instructions (PowerShell)
```powershell
# from repository root
python .\capstone_project\main.py

# or use the wrapper
python .\capstone_project\shopping_list_manager.py
```

Next steps / Ideas
- Track item prices and decrement the `groceries` budget as items are added.
- Persist shopping list and remaining budget to a JSON file.
- Add unit tests for `budget.py` and `shopping_manager.py`.
- Improve CLI UX (remove-by-index, quantities, CSV import/export).

If you'd like, I can implement price-tracking or persistence next — tell me which and I'll add a todo and implement it.
