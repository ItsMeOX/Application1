class Solution:
    def minInsertions(self, s: str) -> int:
        s_rev = s[::-1]
        dp = [[-1] * len(s) for _ in range(len(s))]

        def recursion(i, j):
            if i >= len(s) or j >= len(s):
                return 0
            elif dp[i][j] != -1:
                return dp[i][j]
            elif s[i] == s_rev[j]:
                res = 1 + recursion(i+1, j+1)
            else:
                res = max(recursion(i+1, j), recursion(i, j+1))

            dp[i][j] = res
            return res
        
        return len(s) - recursion(0, 0)


sol = Solution()
print(sol.minInsertions("leetcode"))