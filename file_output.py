source = open("haiku.txt", "r")

# you can read a number of characters
poem_bit = source.read(10)
print(poem_bit)

poem_bit = source.read(10)
print(poem_bit)

source.seek(0)

# You can read line by line

for line in source:
    print(line)

source.seek(0)


list_lines = source.readlines()
print(list_lines)

source.close()