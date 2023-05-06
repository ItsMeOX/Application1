class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        curPrice = prices[0]
        profit = 0
        for price in prices:
            if price > curPrice:
                profit += price - curPrice
            curPrice = price
        return profit
