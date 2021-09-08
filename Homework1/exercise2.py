'''
2. Implement in Python the insertion sort procedure to sort into non-increasing instead of non-decreasing order
    2.1 Use the time function to measure the execution time for the best and worst inputs of size between 10 and 1,000 (use steps of 10)
    2.2 Plot the best and worst execution times measured in (2.1) as a function of $n$
    2.3 Use the random function to generate randomly sorted inputs to calculate the execution time. For each $n$ run the program for 100 different inputs. Do for $n = 100,200, \dots, 1000$.
    2.4 Plot the mean, median, and standard deviation as a function of $n$ for the values obtained in 2.3
'''
import time
import random
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

best_case = []
worst_case = [1,4,1,5,1,2,77,4]

def reversedInsertionSort(arr):
    s = time.time()
    for i in range(1,len(arr)):
        curr = arr[i]
        prev_pos = i - 1

        # Change < to > in second condition to work in reverse
        while prev_pos >= 0 and curr > arr[prev_pos]:
            arr[prev_pos+1] = arr[prev_pos]
            prev_pos -= 1

        arr[prev_pos+1] = curr
    
    return arr, time.time()-s

# best_sorted, best_time = reversedInsertionSort(best_case)
# worst_sorted, worst_time = reversedInsertionSort(worst_case)

exec_times = []

for i in range(10,1000,10):
    arr = []
    arr_size = i
    for j in range(arr_size):
        arr.append(random.randint(1,1001))
    sorted, exec_time = reversedInsertionSort(arr)
    exec_times.append(exec_time)


r = pd.DataFrame()
r['n'] = range(10,1000,10)

r['time_loop'] = [reversedInsertionSort(x) for x in r['n']]
r['time_loop'] = 1000000*r['time_loop']

r.plot(x='n', y='time_loop')
plt.grid()
plt.ylabel('us')
# print(best_time)
# print(worst_time)