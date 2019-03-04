# Python Cheat Sheet

This document will cover the basics of the Python language. It assumes you are familiar with the basics of programming covered in Semester 1, _H6S9 36 Applications Development_. It covers Python 3.

## Contents
- [String input and output](#stringIO)
- [Types and type conversion](#types)
- [Number operators](#numOp)
- [Operator precedence](#bodmas)
- [String Operators](#stringOp)
- [Comparison Operators](#compOp)
- [Boolean Operators](#boolOp)

## Input and Output
### <a name="stringIO"></a>Simple string input and output

Output to the console:

```python
print("Hello this is an output")
```

Input from the console:

```python
name = input("What is your name? ")
```

Remember: `input()` function **on right** saves its result into variable **on left**. This is called an assignment: **= is an assignment operator**, the action to set or save something to a variable.

```python
variable = value
```

### <a name="types"></a>Types and type conversion

Remember, `input()` always returns **a string**.

```python
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

```python
string = "This is a string" # Text              str()
integer = 42 # Whole numbers                    int()
floating_point = 42.35 # Numbers with decimals  float()
boolean = True # True / False
```
## Operators
### <a name="numOp"></a>Number operators

Add

```python
n = 1 + 1
```

Multiply

```python
n = 3 * 5
```

Division (result = float)

```python
n = 3 / 2
```

Integer division (result = int without remainder)

```python
n = 3 // 2
```

Modulo (remainder of integer division)

```python
n = 3 % 2
```

Power (example 3 squared)

```python
n = 3 ** 2
```

### <a name="bodmas"></a>Operator precedence

Remember the PEDMAS rule (Parentheses - Exponents/square Roots - Multiplication/Division - Addition/Subtraction)

E.g. Result: 13
```python
n = 3 + 5 * 2
```

Result: 16
```python
m = (3 + 5) * 2 
```

### <a name="stringOp"></a>String Operators

You can concatenate strings: join them together.

Below will give `"HelloWorld"`
```python
s = "Hello" + "World" # Concatenation ("HelloWorld")
print(s)
```

You can repeat strings using the multiplication operator:
Below would result in `"HelloHelloHelloHello"`:
```python
s = "Hello" * 4
print(s)
```


### <a name="compOp"></a>Comparison Operators

Compares two values / variables. The result is a boolean (`True/False`).

```python
print(3 == 3) # Equality operator
print(3 == 2) # "is equal to"

print(3 > 2)  # Greater than
print(3 >= 3) # Greater than or equal

print(2 < 3)  # Lower than
print(2 <= 2) # Lower than or equal

print(2 != 3) # Different from 
```

### <a name="boolOp"></a>Boolean operators

In python use plain English for and / or / not.
```python
print(True and True) # True
print(True and False) # False
print(True or True) # True
print(not False) # True
print((3 == 3) and (3 == 2)) # False
```

Operator logic follows the **Truth Tables**:

- AND

|    a    |    b     | a AND b  |
| ------- | -------- | -------- |
| `True`  | `True`   | `True`   |
| `True`  | `False`  | `False`  |
| `False` | `True`   | `False`  |
| `False` | `False`  | `False`  |

- OR

|    a    |    b     | a OR b   |
| ------- | -------- | -------- |
| `True`  | `True`   | `True`   |
| `True`  | `False`  | `True`   |
| `False` | `True`   | `True`   |
| `False` | `False`  | `False`  |

- NOT

|    a    |    NOT a |
| ------- | -------- |
| `True`  | `False`  |
| `False` | `True`   |