from collections import deque

def countIslandsBFS(grid):
        
    y_count = len(grid)
    x_count = len(grid[0])

    def bfs(i, j):
        queue = deque()
        queue.append((i, j))
        while queue:
            for k in range(len(queue)):
                i, j = queue.popleft()
                for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if x >= 0 and y >= 0 and x < y_count and y < x_count and grid[x][y] == "1":
                        queue.append((x, y))
                        grid[x][y] = 'X'

    count = 0
    for i in range(y_count):
        for j in range(x_count):
            if grid[i][j] != 'X' and grid[i][j] == '1':
                grid[i][j] = 'X'
                bfs(i, j)
                count += 1

    return count

print(countIslandsBFS([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))