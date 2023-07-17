from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        width, height = len(mat[0]), len(mat)
        
        res = []
        
        temp = [[] for _ in range(width + height - 1)]

        def diagonal(i, row, col): # +1, -1
            while col >= 0 and row < height:
                temp[i].append(mat[row][col])
                row += 1
                col -= 1

        for i in range(width):
            diagonal(i, 0, i)
        
        for j in range(1, height):
            diagonal(i+j, j, width-1)

        for i in range(len(temp)):
            if i % 2 == 0:
                temp[i].reverse()
            res.extend(temp[i])
        
        return res
        