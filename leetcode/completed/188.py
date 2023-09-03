from typing import List

# Same as question 123, except that k is not more a constant.

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        dpb = [[0, 0] for _ in range(k)]

        for i in range(len(prices)-1, -1, -1):
            dpf = [[0, 0] for _ in range(k)]
            for j in range(k):
                dpf[j][1] = max(dpb[j][1], dpb[j][0] - prices[i])
                dpf[j][0] = max(dpb[j][0], (dpb[j+1][1] if j < k-1 else 0) + prices[i])

            dpb = dpf

        return dpf[0][1]


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        dp = [[[0, 0] for _ in range(k+1)] for _ in range(len(prices)+1)]

        for i in range(len(prices)-1, -1, -1):
            for j in range(k):
                dp[i][j][1] = max(dp[i+1][j][1], dp[i+1][j][0] - prices[i])
                dp[i][j][0] = max(dp[i+1][j][0], dp[i+1][j+1][1] + prices[i])
    
        return dp[0][0][1]


from functools import lru_cache
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        @lru_cache(None)
        def dfs(i, cnt, buying):
            if i == len(prices) or cnt == k:
                return 0

            if buying:
                return max(dfs(i+1, cnt, buying), dfs(i+1, cnt, not buying) - prices[i])
            else:
                return max(dfs(i+1, cnt, buying), dfs(i+1, cnt+1, not buying) + prices[i])
        
        return dfs(0, 0, True)