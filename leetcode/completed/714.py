from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int: #DP
        memo = {}
        def dfs(i, buying):
            if i == len(prices):
                return 0
            
            if (i, buying) in memo:
                return memo[(i, buying)]

            if buying:
                memo[(i, buying)] = max(dfs(i+1, not buying)-prices[i], dfs(i+1, buying))
            else:
                memo[(i, buying)] = max(dfs(i+1, not buying)+prices[i]-fee, dfs(i+1, buying))
            
            return memo[(i, buying)]
        
        return dfs(0, True)

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int: # ?
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if min_price > price:
                min_price = price
            elif price - min_price - fee > 0:
                max_profit += price - min_price - fee
                min_price = price - fee
        
        return max_profit
    

sol = Solution()
print(sol.maxProfit(prices = [1,3,2,8,4,9], fee = 2))