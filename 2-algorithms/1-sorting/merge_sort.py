def merge(arr1,arr2): # This is a helper function that takes two sorted list and combine then
    # define and empty list.
    combined = []
    # define two variables i and j to used them with the two lists for the indexes
    i = 0
    j = 0
    # this while loop will run as long as we do get to the last element for one the lists
    while i< len(arr1) and j < len(arr2): 
        # the first loop this compares the first element in arr1 to the first element in arr2 it 
        # it smaller it will push it to combined list, if not it will push the first element in arr2.. and the loop goes on
        if arr1[i]<arr2[j]:
            combined.append(arr1[i])
            i += 1
        else:    
            combined.append(arr2[j])
            j += 1

    while i< len(arr1):
        combined.append(arr1[i])
        i += 1
    while j< len(arr2):
        combined.append(arr2[j])
        j += 1
    return combined
def merge_sort(my_list):
    if len(my_list)==1:
        return my_list
    mid = int(len(my_list)/2)
    left = merge_sort(my_list[mid:])
    right = merge_sort(my_list[:mid])
    return merge(left,right)

original_list = [3,1,4,2]

sorted_list = merge_sort(original_list)
print(sorted_list)