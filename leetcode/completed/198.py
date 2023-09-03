class Solution:
    def rob(self, nums: list[int]) -> int:
        var1, var2 = 0, 0

        for i in range(len(nums)-1, -1, -1):
            t = max(var1, nums[i] + var2)
            var2 = var1
            var1 = t

        return var1

class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = [0] * (len(nums)+2)

        for i in range(len(nums)-1, -1, -1):
            dp[i] = max(dp[i+1], nums[i] + dp[i+2])

        return dp[0]

from functools import lru_cache
class Solution:
    def rob(self, nums: list[int]) -> int:
        @lru_cache(None)
        def dfs(i):
            if i >= len(nums):
                return 0
            
            return max(dfs(i+2) + nums[i], dfs(i+1))

        return dfs(0)