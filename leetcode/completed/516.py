class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rev_s = s[::-1]
        dp = [[-1] * len(s) for _ in range(len(s))]

        def recursive(i, j):
            if i >= len(s) or j >= len(s):
                return 0
            elif dp[i][j] != -1:
                return dp[i][j]
            elif rev_s[i] == s[j]:
                res = 1 + recursive(i+1, j+1)
            else:
                res = max(recursive(i+1, j), recursive(i, j+1))

            dp[i][j] = res
            return res        

        return recursive(0, 0)

sol = Solution()
print(sol.longestPalindromeSubseq("cbbd"))