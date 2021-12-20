import math
def numSquares(n):
    visited = set()
    q = [0]
    count = 0
    mid = int(math.sqrt(n))

    while True:
        count += 1
        q2 = []
        
        for val in q:
            for i in range(mid, 0, -1):
                curr = val + i * i
                if n == curr:
                    return count

                if curr not in visited and curr < n:
                    visited.add(curr)
                    q2.append(curr)

        q = q2

print(numSquares(9))
        