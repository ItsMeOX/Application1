from typing import List
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        memo = [[-1]*len(grid[0]) for _ in range(len(grid))]
        MOD = 10**9 + 7

        def validStep(i,j,prev):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] <= prev:
                return False
            return True

        def dfs(i,j):
            if memo[i][j] != -1:
                return memo[i][j]
            
            curr_paths = 1
            for drow,dcol in [(-1,0),(1,0),(0,-1),(0,1)]:
                if validStep(i+drow, j+dcol, grid[i][j]):
                    curr_paths += dfs(i+drow, j+dcol)
            
            memo[i][j] = curr_paths
            return curr_paths

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if memo[i][j] == -1:
                    dfs(i,j)
                    
        res = 0
        for row in memo:
            res += sum(row)
        return res % MOD



