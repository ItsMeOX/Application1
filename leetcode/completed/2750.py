from typing import List
from functools import lru_cache

# For every i, keep track of ones in current subarray.

# Base cases:
# 1. amount of ones > 1, return 0
# 2. i out of bound    , return there is only one '1' in current subarray.

# For every i, we can either 
# 1. continue without splitting into subarray
# 2. if we have one '1' in our subarray, we can split into subarray.

class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        @lru_cache(5000)
        def dfs(i, ones):
            if ones > 1:
                return 0

            if i == len(nums):
                if ones == 1:
                    return 1
                return 0

            if nums[i] == 1:
                ones += 1
            
            res = dfs(i+1, ones)

            if ones == 1:
                res += dfs(i+1, 0)

            return res

        return dfs(0, 0) % MOD
    

class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        if 1 not in nums: return 0

        res = 1
        prev_index = -1

        for i in range(len(nums)):
            if nums[i] == 1:
                if prev_index == -1:
                    prev_index = i
                else:
                    res *= (i - prev_index)
                    res %= MOD
                    prev_index = i
        
        return res % MOD


        MOD = 10 ** 9 + 7

        @lru_cache(5000)
        def dfs(i, ones):
            if ones > 1:
                return 0

            if i == len(nums):
                if ones == 1:
                    return 1
                return 0

            if nums[i] == 1:
                ones += 1
            
            res = dfs(i+1, ones)

            if ones == 1:
                res += dfs(i+1, 0)

            return res

        return dfs(0, 0) % MOD