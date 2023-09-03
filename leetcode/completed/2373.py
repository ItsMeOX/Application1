from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = []

        for r in range(1, n-1):
            temp = []
            for c in range(1, n-1):
                t = 0
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        t = max(t, grid[r+dr][c+dc])
                temp.append(t)
            res.append(temp)

        return res