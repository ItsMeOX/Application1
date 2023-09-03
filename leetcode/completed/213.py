from typing import List
from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        def houseRobber(nums, start, end):

            @lru_cache(None)
            def dfs(i):
                if i >= end:
                    return 0
                
                return max(nums[i] + dfs(i+2), dfs(i+1))

            return dfs(start)
        
        return max(houseRobber(nums, 0, max(len(nums)-1, 1)), houseRobber(nums, 1, len(nums)))
    
# Same with house robber, but with upper and lower bound limit.

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        def houseRobber(start, end):
            cur = prev = 0

            for i in range(end-1, start-1, -1):
                cur, prev = max(nums[i] + prev, cur), cur
            
            return cur
        
        return max(houseRobber(0, len(nums)-1), houseRobber(1, len(nums)))