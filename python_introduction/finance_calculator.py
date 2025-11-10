#!/usr/bin/env python3

"""
     ============User Input for Financial Details=============

1. Prompt the user for their monthly income: “Enter your monthly income: ”.
    Ask for their total monthly expenses: “Enter your total monthly expenses: ”.

2. Calculate Monthly Savings:
    Calculate the monthly savings by subtracting monthly expenses from the monthly income.

3. Project Annual Savings:
    Assume a simple annual interest rate of 5%.
    Calculate the projected savings after one year, incorporating the interest. Use the simplified formula for annual savings projection: (Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)).
    Output Results:

4. Display the user’s monthly savings.
    Display the projected annual savings after including interest.
"""
"""
=========varianles needed=========
monthly_income
total_monthly_expenses
monthly_savings
projected_savings

where;
(Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)).
 """
# finance_calculator.py

# Ask user to enter their monthly income, ensuring the use of float data type
monthly_income = float(input("Enter your monthly income: "))

# Ask user to enter their total monthly expenses, ensuring the use of float data type
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Projected savings after one year at a simple 5% annual interest rate
interest_rate = 0.05
annual_savings = monthly_savings * 12
projected_savings = annual_savings * (1 + interest_rate)

# Print the results, rounding to two decimal places
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")