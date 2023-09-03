from typing import List

# Starting from any row at column = 0,
# we check if value of grid of next move is > value of current grid.
# If true then 1 + dfs(next grid).

from functools import lru_cache
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(r, c):
            if c == n-1:
                return 0

            res = 0
            for dr in (-1 , 0, 1):           
                if 0 <= r+dr < m and grid[r+dr][c+1] > grid[r][c]:
                    res = max(res, 1 + dfs(r+dr, c+1))

            return res 
    
        res = 0
        for r in range(m):
            res = max(res, dfs(r, 0))
        
        return res
    
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dpb = [0] * m

        for c in range(n-2, -1, -1):
            dpf = [0] * m
            for r in range(m):
                for dr in (-1, 0, 1):
                    if 0 <= r+dr < m and grid[r+dr][c+1] > grid[r][c]:
                        dpf[r] = max(dpf[r], 1 + dpb[r+dr])
            dpb = dpf

        return max(dpf)


        # m, n = len(grid), len(grid[0])

        # @lru_cache(None)
        # def dfs(r, c):
        #     if c == n-1:
        #         return 0

        #     res = 0
        #     for dr in (-1 , 0, 1):           
        #         if 0 <= r+dr < m and grid[r+dr][c+1] > grid[r][c]:
        #             res = max(res, 1 + dfs(r+dr, c+1))

        #     return res 
    
        # res = 0
        # for r in range(m):
        #     res = max(res, dfs(r, 0))
        
        # return res