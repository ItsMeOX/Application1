class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int: # better not modify input
        length = len(matrix)

        for i in range(1, length):
            for j in range(length):
                if j == 0:
                    matrix[i][j] += min(matrix[i-1][j], matrix[i-1][j+1])
                elif j == length - 1:
                    matrix[i][j] += min(matrix[i-1][j-1], matrix[i-1][j])
                else:
                    matrix[i][j] += min(matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1])
        return min(matrix[-1])


# class Solution:
#     def minFallingPathSum(self, matrix: list[list[int]]) -> int:
#         length = len(matrix)
#         dp = [[None for _ in range(length)] for _ in range(length-1)]
#         res = float('inf')

#         def dfs(row, col):
#             if col >= length or col < 0:
#                 return float('inf')

#             if row >= length - 1:
#                 return matrix[row][col]
            
#             if dp[row][col] != None:
#                 return dp[row][col]
            
#             dp[row][col] = matrix[row][col]
#             dp[row][col] += min(dfs(row+1, col-1), dfs(row+1, col), dfs(row+1, col+1))
#             return dp[row][col]

#         for i in range(length):
#             res = min(res, dfs(0, i))

#         return res


sol = Solution()
print(sol.minFallingPathSum([[100,100,100],[100,100,100],[100,100,100]]))