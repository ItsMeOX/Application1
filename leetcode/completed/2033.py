from typing import List

# Get the median of whole grid, then calculate the steps required to
# inc/dec grid[i][j] into median.
# If it cannot be changed into median, return -1.

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])
        flatten = sorted(grid[r][c] for c in range(n) for r in range(m))
        target = flatten[len(flatten)//2]

        res = 0
        for r in range(m):
            for c in range(n):
                if abs(grid[r][c]-target) % x: return -1
                res += abs(grid[r][c]-target) // x

        return res

# [1, 4, 7], k = 3