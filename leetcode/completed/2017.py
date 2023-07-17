from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        prefix = [0] * (len(grid[0])+1)
        suffix = [0] * (len(grid[0])+1)

        for i in range(len(grid[0])):
            prefix[i+1] = prefix[i] + grid[1][i]

        for i in range(len(grid[0])-1, -1, -1):
            suffix[i] = suffix[i+1] + grid[0][i]

        res = float('inf')
        for i in range(len(grid[0])):
            temp = max(prefix[i], suffix[i+1])
            res = min(res, temp)

        return res

# Starting Grid:
# 20 03 20 17 02 12 15 17 04 15 
# 20 10 13 14 15 05 02 03 14 03

# 00 00 00 00 00 12 15 17 04 15
# 20 10 13 14 00 00 00 00 00 00

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        upper, lower, res = sum(grid[0]), 0, float('inf')

        for i, j in zip(grid[0], grid[1]):
            upper -= i
            res = min(res, max(upper, lower))
            lower += j

        return res