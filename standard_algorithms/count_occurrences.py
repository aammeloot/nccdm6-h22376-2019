# Counting occurrences
# An implementation in Python
# By Aurélien 

names = ["Jack","Jason","Jack","Joey","Jack",
"Shane","Jason","Jack","James"]

name_sought = input("What name are you looking for?")

# Counter of occurrences
occurrences = 0

# Every element in the list
for counter in range(len(names)):
    if names[counter] == name_sought:
        occurrences += 1

print(name_sought, "appears", occurrences, "times.")

