from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        one_col = []
        one_row = []

        for row in grid:
            one_row.append(row.count(1))
        
        for col in zip(*grid):
            one_col.append(col.count(1))

        m, n = len(grid), len(grid[0])

        res = []

        for i in range(m):
            res.append([])
            for j in range(n):
                res[-1].append(one_row[i] + one_col[j] - (m - one_row[i]) - (n - one_col[j]))

        return res
