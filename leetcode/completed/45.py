from typing import List
from functools import lru_cache

class Solution:
    def jump(self, nums: List[int]) -> int:

        @lru_cache(None)
        def dfs(i):
            if i == len(nums)-1:
                return 0
            
            t = float('inf')
            for j in range(1, nums[i]+1):
                t = min(t, dfs(i + j))
            
            return t + 1

        return dfs(0)
    
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        dp[-1] = 0

        for i in range(len(nums)-2, -1, -1):
            for j in range(1, nums[i]+1):
                dp[i] = min(dp[i], dp[min(i+j, len(nums)-1)] + 1)

        return dp[0]

# This is like BFS, if we reached the current maximum jumping distance (curMaxDist), 
# then we have to make another jump, hence res += 1 when i == curMaxDist,
# and we have to update current maximum to the new maximum jumping distance.

class Solution:
    def jump(self, nums: List[int]) -> int:
        res = maxDistance = curMaxDist = 0

        for i in range(len(nums)-1):
            maxDistance = max(maxDistance, nums[i]+i)

            if i == curMaxDist:
                curMaxDist = maxDistance
                res += 1
        
        return res


sol = Solution()
print(sol.jump([1,1,5,5,4]))
print(sol.jump([2,3,0,1,4]))
print(sol.jump([2,3,1,1,4]))

