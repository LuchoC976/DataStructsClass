# Linear search implementation

# Input: A (array), element (n)
# Output: Index (i)

def linearSearch(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return None

my_arr = [1,2,3,4,8,9,11]

print(linearSearch(my_arr,5))
