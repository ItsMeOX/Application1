from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        dp = [1] * len(prices)

        for i in range(1, len(prices)):
            if prices[i] == prices[i-1] - 1:
                dp[i] = dp[i-1] + 1

        return sum(dp)

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        prev = 1
        res = 1

        for i in range(1, len(prices)):
            if prices[i] == prices[i-1] - 1:
                prev += 1
            else:
                prev = 1
            res += prev

        return res