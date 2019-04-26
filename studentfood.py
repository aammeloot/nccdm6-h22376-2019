# This about students' favourite food joints

# open file in read mode
f = open("studentfood.csv")

# Read all the file lines and put them in a list
rows = f.readlines()

# Loop -> Goes through all the rows, one by one
for counter in range(len(rows)):
    # Extract the current line
    line = rows[counter].strip() # .strip gets rid of extra whitespace
    # Split the line using , as a separator and save in a list
    fields = line.split(",")

    student_name = fields[0]
    restaurant_name = fields[1]
    amount = fields[2]
    location = fields[3]

    print(30 * "*")
    print("Name:", student_name)
    print("Favourite restaurant:", restaurant_name)
    print("Amount spent: £", amount)
    print("Location:", location)
    print()


