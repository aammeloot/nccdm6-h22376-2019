'''
    Average of a list
    8/3/19
'''

# Create an empty list first
numbers = []
# Individual number, set to zero to enter loop
n = 0

# Repeat until -1 is keyed in:
while n != -1:
    # Get input and convert
    n = int(input("Please enter a number. Type in -1 to finish."))
    # Make sure -1 is not being used in the list
    if n != -1:
        numbers.append(n)

print("Content of the list:", numbers)
total = sum(numbers)
avg = total / len(numbers)
print("The mean is: ", avg)

