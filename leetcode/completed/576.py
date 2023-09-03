from functools import lru_cache

# Base cases:
# 1. out of bound: return 1
# 2. out of moves: return 0

# Starting from start row and start col, dfs to neighbour cells until 
# out of bound or move runs out.

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        directions = ((-1, 0),(1, 0),(0, -1),(0, 1))
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def dfs(r, c, move):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 1

            if move == maxMove: return 0

            res = 0
            for dr, dc in directions:
                res += dfs(r+dr, c+dc, move+1)
            
            return res % MOD

        return dfs(startRow, startColumn, 0) % MOD
    
# slow
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        directions = ((-1, 0),(1, 0),(0, -1),(0, 1))
        MOD = 10 ** 9 + 7

        dpb = [[0]*n for _ in range(m)]

        for k in range(maxMove-1, -1, -1):
            dpf = [[0]*n for _ in range(m)]
            for r in range(m):
                for c in range(n):        
                    for dr, dc in directions:
                        if r+dr < 0 or r+dr >= m or c+dc < 0 or c+dc >= n:
                            dpf[r][c] += 1
                        else:
                            dpf[r][c] += dpb[r+dr][c+dc]
                        dpf[r][c] %= MOD
            dpb = dpf

        return dpb[startRow][startColumn] % MOD