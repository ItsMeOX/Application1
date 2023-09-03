# Base cases:
# If i out of bound, return 0.

# Cases:
# For each index i, we iterate j from i to len(s), and if s[i:j+1] is palindrome, we will try to cut at j and start dfs at j+1,
# each cut we have to add 1 to res.


# Optimization: can reduce time complexity from O(N^3) to O(N^2) by precomputing whether s[i:j+1] is palindrome.
class Solution:
    def minCut(self, s: str) -> int:
        dp = [len(s)] * (len(s)+1)
        dp[-1] = 0
        isPalin = [[False]*(len(s)+1) for _ in range(len(s)+1)]

        for i in range(len(s)):
            j = 0
            while i-j >= 0 and i+j < len(s) and s[i-j] == s[i+j]:
                isPalin[i-j][i+j+1] = True
                j += 1
            
            j = i+1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                isPalin[i][j+1] = True
                j += 1
                i -= 1
        

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if isPalin[i][j+1]:
                    dp[i] = min(dp[i], dp[j+1] + 1)
        
        return dp[0] - 1
    
from functools import cache    
class Solution:
    def minCut(self, s: str) -> int:
        @cache
        def dfs(i):
            if i == len(s):
                return 0
            
            res = float('inf')
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    res = min(res, dfs(j+1) + 1)

            return res

        return dfs(0) - 1
