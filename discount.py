# Program to work out a discount
# Aurelien Ammeloot
# 22 Feb 2019

# Create three main variables as floating-point
price = 0.0
discount = 0.0
deduction = 0.0

# Input of the main price
# We convert string to float
# Example 1: in 2 steps
price = input("Please enter a price: ")
price = float(price)
# Example 2: nested function, all on one line
discount = float(input("Please enter a discount 0-100: "))

# Do the maths
deduction = price / 100 * discount
price = price - deduction

# Show the answer
print("The new price is:", price)
