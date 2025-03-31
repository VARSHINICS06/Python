def greet():
    print("Hello! Welcome to the Python course.")
greet()

# Hello! Welcome to the Python course.

def greet_user(name):
    print(f"Hello, {name}! Welcome to the Python course.")

greet_user("Anand")

# Hello, Anand! Welcome to the Python course.

def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print("The sum is:", result)

# The sum is: 30

def greet(name="Student"):
    print(f"Hello, {name}! Welcome to the Python course.")

greet()  # Uses default value "Student"
greet("Geetha")  # Uses passed value "Geetha"

# Hello, Student! Welcome to the Python course.
# Hello, Geetha! Welcome to the Python course.

#  Local and Global Variables

name = "Global Name"

def greet():
    name = "Local Name"
    print(name)

greet()  # Prints local variable
print(name)  # Prints global variable

# Local Name
# Global Name