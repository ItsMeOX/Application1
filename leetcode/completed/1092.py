
# Here we have to compute the dp table first.
# Then from (m, n), we will traverse pointers i, j back to (0, 0).
# The cases are:
# 1. i == 0, then j - 1 all the way
# 2. j == 0, then i - 1 all the way
# 3. str1[i-1] == str2[j-1] ( not dp[i-1][j] == dp[i][j-1] ! ), then i - 1, j - 1
# 4. dp[i-1][j] == dp[i][j], then i - 1.
# 5. dp[i][j-1] == dp[i][j], then j - 1
# Then we will reverse the string at last.

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        m, n = len(str1), len(str2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        print(*dp, sep='\n')

        res = ''
        i, j = m, n
        while i or j:
            if i == 0:
                res += str2[j-1]
                j -= 1
            elif j == 0:
                res += str1[i-1]
                i -= 1
            elif str1[i-1] == str2[j-1]:
                res += str1[i-1]
                i -= 1
                j -= 1
            elif dp[i-1][j] == dp[i][j]:
                res += str1[i-1]
                i -= 1
            elif dp[i][j-1] == dp[i][j]:
                res += str2[j-1]
                j -= 1
        
        return res[::-1]