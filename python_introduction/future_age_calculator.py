#!/usr/bin/env python3
"""
1. Ask user to input their age
2. Use their age to calculate their current age
3. Assume the current year is 2023
4. Calculate their age by the year 2050
5. Print out the result in a human-readable format: In 2050, you will be [age] years old

"""
"""
1. The script prompts the user for their current age.
2. The user enters their age.
3. The script calculates and prints how old the user will be in 2050.
"""

# Define variables 
age = int(input("Please, what is your age?: "))

# Calculate new age
new_age = age + 27

print(f"In 2050, you will be {new_age} years old")

