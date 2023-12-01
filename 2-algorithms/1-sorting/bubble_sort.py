def bubble_sort(arr):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                sorted = False
                arr[i],arr[i+1] = arr[i+1],arr[i]
    print(arr)      
    return arr  


bubbleSort([1,3,5,75,4,7,8])