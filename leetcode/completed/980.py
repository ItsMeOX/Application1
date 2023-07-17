from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        obstacles = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    src = (i, j)
                elif grid[i][j] == 2:
                    dst = (i, j)
                elif grid[i][j] == -1:
                    obstacles += 1

        grid[src[0]][src[1]] = -1
        def dfs(r, c, cnt):
            if r == dst[0] and c == dst[1]:
                return 1 if cnt == (m*n-obstacles) else 0
            
            res = 0
            for dr, dc in directions:
                if 0 <= r+dr < m and 0 <= c+dc < n and grid[r+dr][c+dc] != -1:
                    grid[r+dr][c+dc] = -1
                    res += dfs(r+dr, c+dc, cnt+1)
                    grid[r+dr][c+dc] = 0

            return res

        return dfs(src[0], src[1], 1)