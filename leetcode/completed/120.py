# class Solution:
#     def minimumTotal(self, triangle: list[list[int]]) -> int:
#         memo = {}
#         def dfs(row = 0, col = 0):
#             if row == len(triangle):
#                 return 0
                
            
#             if (row,col) in memo:
#                 return memo[(row,col)]

#             res = min(dfs(row+1, col) + triangle[row][col], dfs(row+1,col+1) + triangle[row][col])
#             memo[(row,col)] = memo.get((row,col), res)
#             return res
            
#         return dfs()

class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = [0]*(len(triangle[-1])+1)
        for row in triangle[::-1]:
            for i, col in enumerate(row):
                dp[i] = min(dp[i], dp[i+1]) + col

        return dp[0]
    
sol = Solution()
t = [[6],[1,2],[6,8,5],[1,6,9,3],[1,6,8,4,2]]
print(sol.minimumTotal(t))
