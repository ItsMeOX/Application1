class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int: #O(m+n)
        res = 0
        last = 0
        for row in range(len(grid)-1, -1, -1):
            while last < len(grid[0]) and grid[row][last] >= 0:
                last += 1
            if last == len(grid[0]):
                return res
            res += len(grid[0]) - last
            
        return res


class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int: #O(m*n)
        res = 0
        for row in grid:
            for col in range(len(row)-1, -1, -1):
                if row[col] < 0:
                    res += 1
                else:
                    break

        return res