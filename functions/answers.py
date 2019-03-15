# Without return values

# Create a function that receives someone's name and prints its amount of 
# characters.
def count_name(name):
    l = len(name)
    print(l)

count_name("Aurelien")

# Create a function that receives two strings and prints out whether 
# they're identical.
def check_identical(string_a, string_b):
    if string_a == string_b:
        print("Identical")
    else:
        print("Not identical")

check_identical("Hello", "World")
check_identical("Hi", "Hi")

# Create a function that takes an integer in and displays the times table for
# that number (from 1 to 12) -- use of for loop.



# With return values

# Create a function that receives someone's name and prints its amount of 
# characters.
def get_length(name):
    l = len(name)
    return l

n = get_length("Aurelien")
print(n)

# Create a function that receives two strings and prints out whether 
# they're identical.
def is_identical(string_a, string_b):
    if string_a == string_b:
        return True
    else:
        return False

a = is_identical("Hello", "World")
print(a)
b = is_identical("Hi", "Hi")
print(b)