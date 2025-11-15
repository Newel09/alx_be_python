"""
==========Instructions==========

Prompt User for a Number:

Ask the user to input a number for which they want to see the multiplication table: 
Enter a number to see its multiplication table:.
Save it in a variable name number
Generate and Print the Multiplication Table:

Use a for loop to iterate through the numbers 1 to 10.
For each iteration, calculate the product of the user’s number and the iterator (the current number in the loop from 1 to 10).
Print each line of the multiplication table in the format: “X * Y = Z”, where X is the user’s number, 
Y is the current number in the loop, and Z is the product.
"""

start = 1
end = 10

range = range(0, 10+1)

number = int(input("Enter a number to see its multiplication table:"))

#print(f"The multiples of {number} from {start} to {end}:")

print(f"The multiples of {number} from {0, 10}:")

for i in range:
   result = number * i
   print(f"{number} * {i} = {result}")


# for i in range(start, end + 1):
   # print(number * i)

