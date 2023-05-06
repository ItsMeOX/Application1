class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row in range(len(matrix)):
            for col in range(row, len(matrix)):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
            matrix[row].reverse()

        # for i in range(len(matrix)):
        #     matrix[i] = list(reversed(matrix[i]))
        

sol = Solution()
sol.rotate([[1,2,3],[4,5,6],[7,8,9]])