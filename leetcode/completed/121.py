class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least = prices[0]
        maxProfit = 0
        for price in prices:
            if price < least:
                least = price
            if price - least > maxProfit:
                maxProfit = price - least
            
        return maxProfit