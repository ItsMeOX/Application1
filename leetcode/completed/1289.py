from typing import List

# Starting from row r = n-2, grid[r][0~n] += min(grid[r+1][0~n]),
# then take the minimum of grid[0].

# O(n^3)
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)

        for r in range(m - 2, -1, -1):            
            for c in range(m):
                t = float('inf') # do not set this to max value of grid, the sum is > max val of grid.
                for nc in range(m):
                    if nc == c: continue
                    t = min(t, grid[r+1][nc])
                grid[r][c] += t

        return min(grid[0])

# O(n^2)
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)

        for r in range(m - 2, -1, -1):            
            smallest = smaller = float('inf')
            for c in range(m):
                if grid[r+1][c] < smallest:
                    smallest, smaller = grid[r+1][c], smallest
                elif grid[r+1][c] < smaller:
                    smaller = grid[r+1][c]

            for c in range(m):
                if grid[r+1][c] != smallest:
                    grid[r][c] += smallest
                else:
                    grid[r][c] += smaller

        return min(grid[0])
    
# With rolling array
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)

        dp_back = [grid[-1][c] for c in range(m)]

        for r in range(m - 2, -1, -1):          
            dp_front = grid[r].copy()  
            smallest = smaller = float('inf')
            for c in range(m):
                if dp_back[c] < smallest:
                    smallest, smaller = dp_back[c], smallest
                elif dp_back[c] < smaller:
                    smaller = dp_back[c]

            for c in range(m):
                if dp_back[c] != smallest:
                    dp_front[c] = grid[r][c] + smallest
                else:
                    dp_front[c] = grid[r][c] + smaller

            dp_back = dp_front

        return min(dp_back)