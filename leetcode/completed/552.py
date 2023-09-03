
# Base case: i reaches n, we have built a valid attendance record, res += 1.

# For every index i, we have three options:
# 1. put P
# 2. put A
# 3. put L.

from functools import lru_cache
class Solution:
    def checkRecord(self, n: int) -> int:
        @lru_cache(5000)
        def dfs(i, absent, late):
            if i == n:
                return 1
            
            # put 'P'
            res = dfs(i+1, absent, 0)

            # put 'A'
            if not absent:
                res += dfs(i+1, 1, 0)

            # put 'L'
            if late < 2:
                res += dfs(i+1, absent, late+1)

            return res
        
        return dfs(0, 0, 0) % (10**9+7)
    
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7

        dpb = [[1, 1, 1] for _ in range(2)]

        for i in range(n):
            dpf = [[0, 0, 0] for _ in range(2)]
            for j in range(2):
                for k in range(3):
                    dpf[j][k] = dpb[j][0] % MOD
                    if not j:
                        dpf[j][k] += dpb[1][0] % MOD
                    if k < 2:
                        dpf[j][k] += dpb[j][k+1] % MOD

            dpb = dpf

        return dpf[0][0] % MOD