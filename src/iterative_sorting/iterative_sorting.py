# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i, len(arr)):
            # TO-DO: swap
            if arr[j] < arr[smallest_index]:
                temp = arr[smallest_index]
                arr[smallest_index] = arr[j]
                arr[j] = temp
                
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    if not len(arr) or len(arr) == 0:
        return arr
        
    for i in range(0, len(arr) - 1):
        for j in range(0, (len(arr) - 1) - i):
            # compare neighboring elements
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1] # bubble-up lowest element
                arr[j+1] = temp

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
