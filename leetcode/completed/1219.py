from typing import List

# iterate through all grids and start a DFS from each cell, we have to explore every possible ways of walking through the grids, 
# so we need to use backtracking in this problem.

# normal BFS and DFS won't work because it only explores one route, and other there will be other more valued route not explored using normal
# BFS and DFS.

# [1,0,7,0, 0,0],
# [2,0,6,0, 1,0],
# [3,5,6,7, 4,2],
# [4,3,1,0, 2,0],
# [3,0,5,0,20,0]

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = set()

        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or not grid[row][col]:
                return 0

            res = grid[row][col]
            temp = 0

            visited.add((row, col))
            for drow, dcol in directions:
                if (row+drow, col+dcol) not in visited:
                    temp = max(temp, dfs(row+drow, col+dcol))
            visited.remove((row, col))
            
            res += temp

            return res

        res = 0
        for row in range(m):
            for col in range(n):
                res = max(res, dfs(row, col))

        return res
    
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or not grid[row][col]:
                return 0

            res = grid[row][col]
            temp = 0

            grid[row][col] = 0
            for drow, dcol in directions:
                temp = max(temp, dfs(row+drow, col+dcol))
            grid[row][col] = res

            res += temp

            return res

        res = 0
        for row in range(m):
            for col in range(n):
                res = max(res, dfs(row, col))

        return res