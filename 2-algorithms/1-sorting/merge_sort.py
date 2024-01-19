# merge sort - lesson one:

# create a array
arr = [2,9,0,2,7,3,1]
#                                                                 *
#                                                                 *
#                                                                 *
# *****************************************************************
# get the length of that arr
length = len(arr)
print(f"the length is: {length}")
#                                                                 *
#                                                                 *
#                                                                 *
# *****************************************************************
# divide the list by 2. this give you the middle number
# to split the list into 2 lists we use the colon
# we use // to give us an even number.
mid = length//2
print(f"the middle number is: {mid}")
# 
# 
#
# *****************************************************************
# Here to said: store all                        
# the elements from the beginning of the list                       
#  until the middle.
left = arr[:mid]
print(f"left: {left}")
#                                                                 *
#                                                                 *
#                                                                 *
# *****************************************************************
# Here to said: store all 
# the elements from the beginning of the list until the middle
right = arr[mid:]
print(f"right: {right}")
#
#
#


