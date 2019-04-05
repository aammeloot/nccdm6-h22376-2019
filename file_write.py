print("""
Write a Haiku:
The first and third verse need 5 syllables
The middle one needs 7 syllables.""")

destination = open("new_haiku.txt", "a")

for i in range(1, 4):
    line = input("Please enter line" + str(i))
    destination.write(line + '\n')

