class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(word1) or j == len(word2):
                return max(len(word1)-i, len(word2)-j)

            if word1[i] == word2[j]:
                res = dfs(i+1, j+1)
            else:
                left  = dfs(i+1, j)
                right = dfs(i, j+1)
                res = min(left, right) + 1

            memo[(i, j)] = res
            return res

        return dfs(0, 0)
    
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0]*(len(word1)+1) for _ in range(len(word2)+1)]

        for i in range(len(word2)+1):
            for j in range(len(word1)+1):
                if i == 0 or j == 0:
                    dp[i][j] = i+j
                elif word2[i-1] == word1[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

        return dp[-1][-1]
    
sol = Solution()
print(sol.minDistance(word1 = "sea", word2 = "eat"))