class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        memo = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0

            if (i, buying) in memo:
                return memo[(i, buying)]

            if buying:
                memo[(i, buying)] = max(dfs(i+1, not buying) - prices[i], dfs(i+1, buying))
            else:
                memo[(i, buying)] = max(dfs(i+2, not buying) + prices[i], dfs(i+1, buying))
            return memo[(i, buying)]
        return dfs(0, True)

sol = Solution()
print(sol.maxProfit([1,2,3,0,2]))