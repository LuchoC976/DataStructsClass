# Insertion sort implementation in Python

my_arr = [8, 5, 4, 10, 9]

def insertionSort(arr):
    
    for i in range(1,len(arr)):
        curr = arr[i]
        prev_pos = i - 1
        while prev_pos >= 0 and curr < arr[prev_pos]:
            arr[prev_pos+1] = arr[prev_pos]
            prev_pos -= 1
        arr[prev_pos+1] = curr
    
    return arr

print("The original array is: " + str(my_arr))
print("The sorted array is: " + str(insertionSort(my_arr)))
