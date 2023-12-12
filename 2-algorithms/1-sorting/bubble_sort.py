
def bubble_sort():
    arr = [1,3,0,75,4,7,8]
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr)-1):
            print(arr[i], arr[i+1])
            if arr[i]>arr[i+1]:
                # arr[i],arr[i+1] = arr[i+1],arr[i]
                # temp = arr[i]
                # arr[i] = arr[i+1]
                # arr[1+1] =  temp
                sorted = False    
    print(arr)      
    return arr  

bubble_sort()



