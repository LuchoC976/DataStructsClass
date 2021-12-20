def countIslandsDFS(grid):

    def dfs(i,j):
        
        grid[i][j] = '0'
        # Arriba
        if grid[i - 1][j] == '1' and i - 1 >= 0:
            dfs(i - 1, j)
        # Derecha
        if j + 1 <= len(grid[0]) - 1 and grid[i][j + 1] == '1':
            dfs(i, j + 1)
        # Abajo
        if i + 1 <= len(grid) - 1 and grid[i + 1][j] == '1':
            dfs(i + 1, j)
        # Izquierda
        if grid[i][j - 1] == '1' and j - 1 >= 0:
            dfs(i, j - 1)
        
    
    count = 0
    size = len(grid)
    for i in range(size):
        for j in range(len(grid[i])):
            if grid[i][j]=='1':
                dfs(i, j)
                count += 1
    return count
    
print(countIslandsDFS([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))