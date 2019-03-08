'''
    Standard algorithms: finding minimum/maximum
    8 March 2019
'''

# List we need

scores = [10, 55, 36, 20, 100, 20]

# Find maximum

# Set a variable, assume maximum is first value
maximum = scores[0] # In our case, set to 10
# Start for loop on list, from SECOND value
for counter in range(1, len(scores)):
    # Check if current value in list is larger than
    # the assumed maximum currently held
    if scores[counter] > maximum:
        # If it is the case, replace the currently
        # assumed maximum with the current list value
        maximum = scores[counter]

# Display result or do anything else...
print("The largest value in list:", scores)
print("is", maximum)