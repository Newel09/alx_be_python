#!/usr/bin/env python3
"""
1. Ask user to input their age
2. Create a file named future_age_calculator.py.
3. Prompt the user to input their current age with the question: “How old are you? ”.
4. Use their age to calculate their current age
5. Assume the current year is 2023
6. Calculate their age by the year 2050
7. Print out the result in a human-readable format: In 2050, you will be [age] years old

"""
"""
1. The script prompts the user for their current age.
2. The user enters their age.
3. The script calculates and prints how old the user will be in 2050.
"""

# Define variables 
age = int(input("How old are you? "))

# Calculate new age
new_age = age + 27

print(f"In 2050, you will be {new_age} years old")

