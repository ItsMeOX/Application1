from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dpb = [[0, 0], [0, 0]]

        for i in range(len(prices)-1 , -1, -1):
            dpf = [[0, 0], [0, 0]]
            for j in range(0, 2):
                dpf[j][1] = max(dpb[j][1], dpb[j][0] - prices[i])
                dpf[j][0] = max(dpb[j][0], (dpb[j+1][1] if j == 0 else 0) + prices[i])

            dpb = dpf

        return dpf[0][1]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = [[[0, 0], [0, 0], [0, 0]] for _ in range(len(prices)+1)]

        for i in range(len(prices)-1 , -1, -1):
            for j in range(0, 2):
                dp[i][j][1] = max(dp[i+1][j][1], dp[i+1][j][0] - prices[i])
                dp[i][j][0] = max(dp[i+1][j][0], dp[i+1][j+1][1] + prices[i])

        return dp[0][0][1]


# If number of completed transactions == 2, then we will return 0, as we cannot make any more transactions.

# If we are not holding stock, then we can either 
# 1. buy  dfs(i+1, cnt, not buying) - prices[i]
# 2. skip dfs(i+1, cnt, buying)

# If we are holding stock, then we can either
# 1. sell dfs(i+1, cnt+1, not buying) + prices[i]
# 2. skip dfs(i+1, cnt, buying)

from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        @lru_cache(None)
        def dfs(i, cnt, buying):
            if i == len(prices) or cnt == 2:
                return 0

            if buying: # not holding stock
                return max(dfs(i+1, cnt, buying), dfs(i+1, cnt, not buying) - prices[i])
            else:
                return max(dfs(i+1, cnt, buying), dfs(i+1, cnt+1, not buying) + prices[i])

        return dfs(0, 0, True)