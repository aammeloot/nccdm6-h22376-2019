'''
    8 March 2019
    List examples
'''

# List = square brackets
# Values separated by commas
# ages is a list of integers
ages = [28, 19, 19, 16, 16, 17, 29, 25, 19, 21, 18, 18, 19, 19, 20, 26, 17, 36, 26]

# For reference, tuples: read-only lists
ages_readonly = (28, 19, 19, 16, 16, 17, 29, 25, 19, 21, 18, 18, 19, 19, 20, 26, 17, 36, 26)

# In a list you can do:
# Find out how many elements?
n = len(ages)
print(n)
# Print a whole list at once
print(ages)
# Add elements to a list
ages.append(30)
print(len(ages))
print(ages)
# Reverse a list
ages.reverse()
print(ages)

# Elements in the list have positions
# First element in position 0
# Second in position 1
# Nth elemenet in position n-1
# Last element in position -> length of list-1

# Go through elements
# With a counter variable
for i in range(len(ages)): # For loop
    print("Position", i, "Value", ages[i])

# Go through elements
# No counter needed
for number in ages:     # Foreach
    print("Age: ", number)

# Do the average
# Remove the 30 that was added earlier
ages.remove(30)
# Create a variable set to zero
total = 0
for n in ages:
    total += n # increment total with current value
print("Average: ", total / len(ages))

# Alternatively
total = sum(ages)




