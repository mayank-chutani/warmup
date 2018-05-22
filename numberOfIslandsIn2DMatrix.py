class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        visited = [['0' for i in range(col)] for j in range(row)]
        rowCheck = [-1, -1, -1, 0, 0, 1, 1, 1]
        colCheck = [-1, 0, 1, -1, 1, -1, 0, 1]
        islandCount = 0
        for i in range(row):
            for j in range(col):
                if (visited[i][j] == '1'):
                    continue
                if (grid[i][j] == '1' and visited[i][j] == '0'):
                    self.dfs(grid, visited, i, j, rowCheck, colCheck, row, col)
                    islandCount += 1
        return islandCount

    def dfs(self, grid, visited, i , j, rowCheck, colCheck, row, col):
        visited[i][j] = '1'
        for p, q in zip(rowCheck, colCheck):
            rowIndex = p + i
            if not (-1 < rowIndex < row):
                continue
            colIndex = q + j
            if not (-1 < colIndex < col):
                continue
            if (visited[rowIndex][colIndex] == '0' and grid[rowIndex][colIndex] == '1'):
                self.dfs(grid, visited, rowIndex, colIndex, rowCheck, colCheck, row, col)
        return 
