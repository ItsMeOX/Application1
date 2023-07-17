from typing import List

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        res = [[0]* n for _ in range(m)]

        for i, val in enumerate(colSum):
            res[0][i] = val
        
        for i in range(m-1):
            j = 0
            current_rowSum = sum(res[i])
            while current_rowSum > rowSum[i]:
                delta = min(res[i][j], current_rowSum - rowSum[i])
                res[i+1][j] += delta
                res[i][j] -= delta
                current_rowSum -= delta
                j += 1
        
        return res