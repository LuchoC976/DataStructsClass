# Insertion sort implementation in Python

my_arr = [8, 5, 4, 10, 9]

def insertionSort(arr):
    
    for i in range(1,len(arr)):
        # Setting position marker for sorted array
        curr = arr[i]
        prev_pos = i - 1

        # Organize unsorted array into sorted one
        while prev_pos >= 0 and curr < arr[prev_pos]:
            # Switch unsorted places
            arr[prev_pos+1] = arr[prev_pos]
            prev_pos -= 1

        # Update marker
        arr[prev_pos+1] = curr

print("The original array is: " + str(my_arr))
print("The sorted array is: " + str(insertionSort(my_arr)))
