# records / dictionaries: 
# records or dictionaries are used to stored related data: like student data:
student = {
    #key | :  value 
    "name":"Khlaid Mohammed",
    "age":14,
    "grade":10
}
# records have keys and values seperated by a colon
# if you want to access anything inside of the record you do:
# Record["key"] like: student["name"] this will give us the name of the student

# ***********list and records************
# if we have more than one studen we can use the list to store more that one record:
students = [
    # the first student
 {
    #key | :  value 
    "name":"Khlaid Mohammed",
    "age":14,
    "grade":10
},
    # the second student
 {
    #key | :  value 
    "name":"Khlaid Mohammed",
    "age":14,
    "grade":10
}

]
# we can use a for loop with this list:
    #student   students
for student in students:
    print(student) # here we are looping over all the record. so we can do anything we want 