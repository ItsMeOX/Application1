class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for _ in range(len(text1))] for _ in range(len(text2))]
        def recursive(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            elif dp[j][i] != -1:
                return dp[j][i]
            elif text1[i] == text2[j]:
                res = 1 + recursive(i+1, j+1)
            else:
                res = max(recursive(i+1, j), recursive(i, j+1))
            dp[j][i] = res

            return res

        return recursive(0, 0)


text1 = "aabbaaaaab"
text2 = "aaaaaaaaaa"
sol = Solution()
print(sol.longestCommonSubsequence(text1, text2))