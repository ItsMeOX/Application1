from typing import List

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        res = []

        for col in zip(*grid):
            max_len = 0
            for digit in col:
                max_len = max(max_len, len(str(digit)))
            res.append(max_len)

        return res