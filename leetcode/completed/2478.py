# Base cases:
# 1. i reaches len(s), only return 1 if current interval is closed and number of interval == k.
# 2. i > len(s), return 0.

# Cases:
# For every i, 
# If we are in middle of unclosed intervals:
# 1. we can either continue without closing interval.
# 2. or we can close interval if s[i] is a non-prime.

# If we are are not in interval and we have to open interval:
# 1. if s[i] is not prime number, return 0.
# 2. else, open a interval and jump to i+minLength-1 as s[i ~ i+minLength-2] this is invalid interval.

from functools import cache
class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        prime = '2357'
        MOD = 10 ** 9 + 7

        @cache
        def dfs(i, intervals, started):
            if i == len(s):
                if started: return 0
                return 1 if intervals == k else 0
            
            if intervals > k or i > len(s):
                return 0
            
            if not started:
                if s[i] in prime:
                    return dfs(i+minLength-1, intervals, True)
                else:
                    return 0
            else:
                res = dfs(i+1, intervals, started)
                if s[i] not in prime:
                    res += dfs(i+1, intervals+1, False)

            return res % MOD

        return dfs(0, 0, False) % MOD
    

class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        prime = '2357'
        MOD = 10 ** 9 + 7
        dpb = [[0]*2 for _ in range(len(s)+1)]
        dpb[-1][0] = 1

        for intervals in range(k-1, -1, -1):
            dpf = [[0]*2 for _ in range(len(s)+1)]
            for i in range(len(s)-1, -1, -1):
                dpf[i][1] = dpf[i+1][1]
                if s[i] not in prime:
                    dpf[i][1] += dpb[i+1][0]
                
                if s[i] in prime:
                    if i+minLength-1 <= len(s):
                        # take note that dpf[x][1] has to be computed beforehand
                        dpf[i][0] = dpf[i+minLength-1][1]
                else:
                    dpf[i][0] = 0
                
                dpf[i][1] %= MOD
                dpf[i][0] %= MOD

            dpb = dpf
        
        return dpf[0][0]