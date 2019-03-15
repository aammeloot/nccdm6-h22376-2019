# Parameters
# process is called parameter passing.
# It sends a duplicate of the original 
# Except for lists, dictionaries etc.

# Simple function with two parameters and no return value
def add(a, b):  # Placeholders: formal parameters
    print(a + b)

# Return value -> sends result outside the function to caller
def multiply(a, b):
    c = a * b
    return c

# Functions can contain any code
def can_drive(age, car):
    if age >= 17:
        return True
    else:
        return False

# Functions can be used for batch process
def unit_grade(marks):
    if marks >= 70:
        return "Pass"
    elif marks >= 45:
        return "Remediation"
    else:
        return "Fail"

marks = [60, 50, 70, 80, 45, 35, 80, 64, 32]
for x in marks:
    print(unit_grade(x))











number = input("Please enter a number")
number = int(number)
anothernumber = int(input("Please enter another."))
# Call the function
#add(number, anothernumber) # Actual parameters

result = multiply(number, anothernumber)
print(result)
