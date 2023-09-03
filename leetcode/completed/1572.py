from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        n = len(mat)
        for r in range(n):
            res += mat[r][r] + mat[r][n-r-1]
        
        if n & 1: res -= mat[n//2][n//2]

        return res