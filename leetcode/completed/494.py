from typing import List

from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @lru_cache(None)
        def dfs(i, cur):
            if i == len(nums):
                return cur == target
            
            return dfs(i+1, cur-nums[i]) + dfs(i+1, cur+nums[i])
        
        return dfs(0, 0)
            
# Here we set the size of column to be total*2+1 because we want to offset and make 
# dp[i][0 ~ total-1] = for negative numbers,
# dp[i][total] = 0,
# dp[i][0 ~ total-1] = for positive numbers.
# Offset dp array by total, so set the target + total to be 1.
# For every nums[i],
# dp[0 ~ nums[i]-1] are for negative values,
# dp[0 + nums[i]] = 0
# dp[nums[i+1] ~ total*2+1] are for positive values.

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total: return 0

        dp = [[0] * (total*2+1) for _ in range(len(nums)+1)]
        dp[-1][target + total] = 1

        for i in range(len(nums)-1, -1, -1):
            for j in range(nums[i], total*2+1-nums[i]):
                dp[i][j] = dp[i+1][j - nums[i]] + dp[i+1][j + nums[i]]

        return dp[0][total]
    

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total: return 0

        dpb = [0] * (total*2+1)
        dpb[target + total] = 1

        for i in range(len(nums)-1, -1, -1):
            dpf = [0] * (total*2+1)
            for j in range(nums[i], total*2+1-nums[i]):
                dpf[j] = dpb[j - nums[i]] + dpb[j + nums[i]]
            dpb = dpf

        return dpf[total]