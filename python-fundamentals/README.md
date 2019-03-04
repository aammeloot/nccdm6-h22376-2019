# Python Cheat Sheet

This document will cover the basics of the Python language. It assumes you are familiar with the basics of programming covered in Semester 1, _H6S9 36 Applications Development_. It covers Python 3.

## Input and Output
### Simple string input and output

Output to the console:

```
print("Hello this is an output")
```

Input from the console:

```
name = input("What is your name? ")
```

Remember: ```input()``` function **on right** saves its result into variable **on left**. This is called an assignment: **= is an assignment operator**, the action to set or save something to a variable.

```
variable = value
```

### Types and type conversion

Remember, ```input()``` always returns **a string**.

```
# Type conversion string to Integer
num1 = int(input("Enter a number")) # Input and convert
num2 = int(input("Enter another number"))
num3 = num1 + num2
print(num3)

# Output of integer
# print can take several arguments:
print("The result is", num3) 

# If you want to concatenate a string with a number you need to convert back:
print("The result is " + str(num3)) 

# You can also use the .format()
print("The result is {}".format(num3))
```

### Data types

```
string = "This is a string" # Text              str()
integer = 42 # Whole numbers                    int()
floating_point = 42.35 # Numbers with decimals  float()
boolean = True # True / False
```

### Number operators

Add

```
n = 1 + 1
```

Multiply

```
n = 3 * 5
```

Division (result = float)

```
n = 3 / 2
```

Integer division (result = int without remainder)

```
n = 3 // 2
```

Modulo (remainder of integer division)

```
n = 3 % 2
```

Power (example 3 squared)

```
n = 3 ** 2
```

### Operator precedence

Result: 13
```
n = 3 + 5 * 2
```

Result: 16
```
m = (3 + 5) * 2 # 16
```

#### String ####

s = "Hello" + "World" # Concatenation ("HelloWorld")
print(s)

### Comparison ###
# Compare two values
# Result is a boolean

print(3 == 3) # Equality operator
print(3 == 2) # "is equal to"

print(3 > 2)  # Greater than
print(3 >= 3) # Greater than or equal

print(2 < 3)  # Lower than
print(2 <= 2) # Lower than or equal

print(2 != 3) # Different from 

### Boolean operators ###

print(True and True)
print(True and False)
print(True or True)
print(not False)

print((3 == 3) and (3 == 2))
