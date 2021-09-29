# Fibonacci example O(n)
# Optimized with duplicate calculations (memoization: cache)

def fib(n):

    cache = {}

    def recursive_fib(n):
        if n in cache.keys():
            return cache[n]
        
        if n == 0 or n == 1:
            res = n
        else:
            res = recursive_fib(n-1) + recursive_fib(n-2)
        
        cache[n] = res
        return res
    
    return recursive_fib(n)

print(fib(5))
print(fib(6))
print(fib(24))
