class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        dpb = [0] * (len(t)+1)
        dpb[-1] = 1

        for i in range(len(s)-1, -1, -1):
            dpf = [0] * (len(t)+1)
            dpf[-1] = 1
            for j in range(len(t)-1, -1, -1):
                if s[i] == t[j]:
                    dpf[j] = dpb[j+1]
                dpf[j] += dpb[j]
            dpb = dpf

        return dpf[0]
    
    

class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][-1] = 1

        for i in range(len(s)-1, -1, -1):
            for j in range(len(t)-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1]
                dp[i][j] += dp[i+1][j]

        return dp[0][0]



# Initialize two pointers i for s, j for t.

# Base cases:
# If j reaches length of t, that means we have a substring equal to t, so return 1.
# If i reaches length of i, then it is invalid, so return 0.

# If s[i] == t[j], i++, j++.
# Always i++ so that we can check if s[i:] has a substring equals to t[j:].

from functools import lru_cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        @lru_cache(None)
        def dfs(i, j):
            if j == len(t):
                return 1
            
            if i == len(s):
                return 0

            res = 0
            if s[i] == t[j]:
                res = dfs(i+1, j+1)
            
            return res + dfs(i+1, j)

        return dfs(0, 0)