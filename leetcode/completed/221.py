class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        side = 0

        
        if "1" in matrix[0]:
            side = 1

        for i in range(row):
            if matrix[i][0] == "1":
                side = 1
                    
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == "1":
                    matrix[i][j] = min(int(matrix[i-1][j]), int(matrix[i][j-1]), int(matrix[i-1][j-1])) + 1
                    side = max(side, matrix[i][j])

        return side ** 2

sol = Solution()
print(sol.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))