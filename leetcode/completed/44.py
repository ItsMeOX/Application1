
# Base cases:
# 1. if i == end and j == end, true
# 2. if i != end and i == end, return false
# 3. if i == end and j != end, we have to check if from j to end of p are all '*'.

# Conditions:
# 1. if s[i] == p[j] or p[j] == '?', we can skip to next index
# 2. if p[j] == '*', we can move i to next index or j to next index.


from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @lru_cache(None)
        def dfs(i, j):
            if i == len(s) and j == len(p):
                return True
            
            if j == len(p):
                return False

            if i == len(s):
                return all(c == '*' for c in p[j:])
            
            if s[i] == p[j] or p[j] == '?': 
                return dfs(i+1, j+1)

            elif p[j] == '*':
                return dfs(i+1, j) or dfs(i, j+1)

            return False

        return dfs(0, 0)
    

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dpb = [False] * (len(p)+1)

        for j in range(len(p)):
            if p[j] == '*':
                dpb[j] = all(c == '*' for c in p[j:])

        dpb[-1] = True

        for i in range(len(s)-1, -1, -1):
            dpf = [False] * (len(p)+1)
            for j in range(len(p)-1, -1, -1):
                if s[i] == p[j] or p[j] == '?':
                    dpf[j] = dpb[j+1]
                elif p[j] == '*':
                    dpf[j] = dpb[j] or dpf[j+1]
            dpb = dpf

        return dpb[0]