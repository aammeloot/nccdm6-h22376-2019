# Example of input and output in Python

# Output to the console:
print("Hello this is an output")

# Input from the console:
name = input("What is your name? ")

# Input Function on right saves its result into variable on left
# This is called an assignment
# = is an assignment operator
# The action to set or save something to a variable
# variable = value

# Input always gives a string

###### Type conversion ###########

num1 = int(input("Enter a number"))
num2 = int(input("Enter another number"))
num3 = num1 + num2
print(num3)

###### Formatted output ##########
print("The result is", num3)
print("The result is " + str(num3))
print("The result is {}".format(num3))

