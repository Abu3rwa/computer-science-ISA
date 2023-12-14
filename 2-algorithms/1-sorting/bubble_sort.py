# bubble sort algorith
def bubble_sort():
    arr = [8,3,0,75,4,7,8]
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr)-1):
             if arr[i]>arr[i+1]:
                sorted = False  
                arr[i],arr[i+1] = arr[i+1],arr[i]
    print(arr)      
    return arr  
bubble_sort()

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







# variable declaration: declaring a name of a variable without giving it a value.
name
# variable initialization: giving the valiable a value when you make it.
name = "Khalid"


