from typing import List

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        isOdd = [[False]*n for _ in range(m)]

        for row, col in indices:
            for i in range(m):
                isOdd[i][col] = not isOdd[i][col]
            for j in range(n):
                isOdd[row][j] = not isOdd[row][j]

        res = 0
        for row in isOdd:
            res += row.count(True)

        return res