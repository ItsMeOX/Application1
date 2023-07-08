from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [[0]*(col+1) for _ in range(row+1)]
        res = 0

        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1]) + 1
                    res += dp[i][j]
        
        return res
    
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp_back = [0] * (col+1)
        res = 0

        for i in range(row-1, -1, -1):
            dp_front = [0] * (col+1)
            for j in range(col-1, -1, -1):
                if matrix[i][j] == 1:
                    dp_front[j] = min(dp_back[j], dp_back[j+1], dp_front[j+1]) + 1
                    res += dp_front[j]
            dp_back = [k for k in dp_front]
        
        return res