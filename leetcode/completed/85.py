from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        row_len, col_len = len(matrix), len(matrix[0])
        
        col_arr = [[0] * col_len for _ in range(row_len)]
        stack = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    stack.append(j)
                if j+1 == col_len or matrix[i][j+1] == "0":
                    while stack:
                        col_arr[i][stack.pop()] = j
        
        for row in col_arr:
            print(row)

        
        stack = []


mat = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
sol = Solution()
print(sol.maximalRectangle(mat))