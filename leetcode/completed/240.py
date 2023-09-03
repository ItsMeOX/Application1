from typing import List

# O(m*n)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target in row:
                return True

        return False
    
# O(m+n)
# Intuition:
# Starting at top right corner, 
# if target > matrix[row][col], then we can discard current row, so move row to row+1.
# if target < matrix[row][col], then we can discord current col, so move col to col-1.
# If target is equal to matrix[row][col], that means we have found the target, return true.
# If our pointer is out of bound, then that means target is not in matrix.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0])-1

        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            
            if matrix[row][col] > target:
                col -= 1
            else:
                row += 1

        return False