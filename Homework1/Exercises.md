## 1. Sort the following functions in decreasing order of asymptotic complexity ($O(f(n))$):
- $f_1(n) = n^{\sqrt{n}}$
- $f_2(n) = 2^n$
- $f_3(n) = {n\choose 2}$
- $f_4(n) = \sum_{i=2}^n (i-1)$

### Answer:
#### $f_2(n) \leq f_1(n) \leq f_4(n) \leq f_3(n)$
--------
## 2. Implement in Python the insertion sort procedure to sort into non-increasing instead of non-decreasing order
- 2.1 Use the time function to measure the execution time for the best and worst inputs of size between 10 and 1,000 (use steps of 10)
- 2.2 Plot the best and worst execution times measured in (2.1) as a function of $n$
- 2.3 Use the random function to generate randomly sorted inputs to calculate the execution time. For each $n$ run the program for 100 different inputs. Do for $n = 100,200, \dots, 1000$.
- 2.4 Plot the mean, median, and standard deviation as a function of $n$ for the values obtained in 2.3
### Answer:
#### See exercise2.py for answer
--------
## 3. CLRS 2.1-4
pg. 22: Consider the problem of adding two n-bit binary integers, stored in two n-element arrays A and B. The sum of the two integers should be stored in binary form in an .n C 1/-element array C. State the problem formally and write pseudocode for adding the two integers.
### Answer:
#### Input:
$A = [a_1,a_2,\dotsc,a_n]$ where $a_n$ are booleans,

$B= [b_1,b_2,\dotsc,b_n]$ where $b_n$ are booleans

Output:
$C = [c_1,c_2,\dotsc,c_{n+1}]$ where $c_n$ is the sum of $a_n + b_n$  
####
#### Pseudocode:
    function bin_sum(A,B):
        C = int[A.length + 1]
        carry = 0
        for i = 1 to A.length:
            C[i] = (A[i] + B[i] + carry) % 2 
            carry = (A[i] + B[i] + carry) / 2
        C[i + 1] = carry
        return C
--------
## 4. CLRS 3.1-1
pg. 52

### Answer:

--------
## 5. CLRS 3.1-2
pg. 52

### Answer:

--------
## 6. CLRS 3.1-6
pg. 53

### Answer:

--------
## 7. CLRS 3-4 (a,b,e,g)
pg. 62

### Answer: