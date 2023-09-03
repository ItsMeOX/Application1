
# For every character in s, we can do the following:
# 1. convert this number to character
# 2. convert this + next number to character
# For (1) to be valid, we need to make sure s[i] is not 0.
# For (2) to be valid, we need to make sure that 0 <= (s[i] + s[i+1]) <= 26.
# Whenever i reaches length of s, we have successfully decoded s, so add 1 to res.

class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i):
            if i > len(s):
                return 0

            if i == len(s):
                return 1
            
            if i in memo:
                return memo[i]

            res = 0
            if s[i] != '0':
                res = dfs(i+1)
            
                if s[i] == '1' or (i+1 < len(s) and s[i] == '2' and s[i+1] in '0123456'):
                    res += dfs(i+2)
            
            memo[i] = res

            return res
        
        return dfs(0)