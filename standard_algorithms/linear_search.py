# Linear search demo, 6 nations edition

nation = ["England", "Scotland", "Wales", "Ireland", "France", "Italy"]

# Create two variable, a flag to signal it's been found (default: False)
# And a counter for the position in the list
item_found = False
counter = 0

# Enquire what we want
desired_item = input("What are you looking for?")

# Search loop
# Continuing condition
while not item_found and counter < len(nation):
    # Compare search term with current value
    if desired_item == nation[counter]:
        print("The program found", desired_item, "at", counter)
        item_found = True
    # Increase counter
    counter += 1

if not item_found:
    print(desired_item, "has not been found.")