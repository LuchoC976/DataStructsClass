# 1. Given a sorted integer array nums and three integers a,
# b and c, apply a quadratic function of the form 
# f(x) = ax2 + bx + c to each element nums[i] in the array, 
# and return the array in a sorted order.

#

import unittest

def TestValue_results():
    assert solve([-4,-2,2,4], 1, 3, 5) == [3,9,15,33], "Should be [3,9,15,33]"
    assert solve([-4,-2,2,4], -1, 3, 5) == [-23,-5,1,7], "Should be [-23,-5,1,7]"
    assert solve([1,2,3,4], 0, 0, 0) == [0,0,0,0], "Should be [0,0,0,0]"
    assert solve([3,-1,4,-7], -1, 3, 4) == [-66,0,0,4], "Should be [-66,0,0,4]"
    assert solve([-2,5,-1,1], 0, 7, -3) == [-17,-10,4,32], "Should be [-17,-10,4,32]"

def solve(nums, a, b, c):
    final = []
    for num in nums:
        final.append(cuadraticSolver(num, a, b, c))
    
    final.sort()
    return final

def cuadraticSolver(num, a, b, c):
    return a * (num**2) + b * num + c

if __name__ == "__main__":
    TestValue_results()
    print("All test cases passed")

'''
Este problema no fue tan complejo, se utiliza la funcion solve() con sus
4 argumentos y se realiza un lazo en donde se calculara el valor para cada
caso (con la funcion cuadraticSolver()), y esos datos se insertan al arreglo
que se va a retornar pero antes de ese paso, se los ordena para determinar
cual es el orden ascendente.
'''
