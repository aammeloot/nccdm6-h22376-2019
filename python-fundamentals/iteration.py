### Conditional loop ###
'''
# Simple condition
age = int(input("How old are you?"))
while age < 18:
    print("Sorry a bit too early to head to the pub.")
    age = int(input("How old are you?"))

print("Let's go now.")

# Input validation with complex condition
num = int(input("Enter a number between 1 and 10"))
while num < 1 or num > 10: # truth table, either needs to be true
    num = int(input("Enter a number between 1 and 10"))

print("You entered", num)

### For loop ### 
'''

for i in range(10):  # From zero to 9
    print("Hello", i)
print()

for i in range(1,11):# range(start, finish)
    print("Hello", i)
print()

for i in range(0,10,2): # range(start, finish, step)
    print("Hello", i)
print()

for i in range(10, 0, -1): #
    print("Hello", i)
print()

for c in "Shane is yawning."*4:
    print(c)

#print("Shane is yawning" * 4)

print("Hello")