# class Solution:
#     def minimumDeleteSum(self, s1: str, s2: str) -> int:
#         total = 0
#         for chr in s1:
#             total += ord(chr)

#         for chr in s2:
#             total += ord(chr)

#         dp = [[0] * len(s1) for _ in range(len(s2))]

#         def dfs(i, j):
#             if i == len(s1) or j == len(s2):
#                 return 0
            
#             if dp[j][i]:
#                 return dp[j][i]
            
#             if s1[i] == s2[j]:
#                 dp[j][i] = ord(s1[i]) + dfs(i+1, j+1)
#             else:
#                 dp[j][i] = max(dfs(i+1,j), dfs(i,j+1))

#             return dp[j][i]

#         return total - 2 * dfs(0, 0)
        
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0] * (len(s1)+1) for _ in range(len(s2)+1)]

        for i in range(1, len(s2)+1):
            for j in range(1, len(s1)+1):
                if s1[j-1] == s2[i-1]:
                    dp[i][j] += dp[i-1][j-1] + ord(s1[j-1])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return sum(map(ord, s1 + s2)) - 2 * dp[-1][-1]

sol = Solution()
print(sol.minimumDeleteSum("sea", "eat"))