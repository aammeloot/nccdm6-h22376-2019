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

# Input validation: ensure price is positive
while price < 0:
    print("Your value is invalid.")
    print("Ensure your price is over 0.")
    price = float(input("Enter new price: "))

# Example 2: nested function, all on one line
discount = float(input("Please enter a discount 0-100: "))

# Input validation: ensure discount in 0 - 100 bracket
while discount < 0 or discount > 100:
    print("Your value is invalid.")
    print("Ensure your discount is in the range 0 - 100")
    discount = float(input("Enter new discount: "))

# Do the maths
deduction = price / 100 * discount
price = price - deduction

# Show the answer
print("The new price is:", price)
