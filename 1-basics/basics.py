# Creating variable and storing value.
variable_name = "Python Programming"

# Printing the values of a variable.
print(variable_name)

# Data types
string_variable = "Hello World"
integer_variable = 10
float_variable = 12.34

# Defining functions and invoking them to run the code inside of them.
def add_numbers(a, b):
    return a + b

print(add_numbers(3, 5))

# Working with parameters and passing argument when calling/ invoking the function.
def multiply_numbers(a, b):
    return a * b

print(multiply_numbers(3, 5))

# Working with lists in python.
fruits = ['apple', 'banana', 'cherry']

# Adding elements to the list.
fruits.append('orange')

# How to access element using the index.
print(fruits[0])

# Removing elements from the list.
fruits.remove('banana')

# Working loops: for loop and while loop.
for i in range(5):
    print(i)

# Using if, elif and else statement.
number = 5

if number > 10:
    print("Number is greater than 10")
elif number < 10:
    print("Number is less than 10")
else:
    print("Number is equal to 10")