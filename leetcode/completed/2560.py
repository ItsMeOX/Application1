from typing import List

# Apply binary search from min of nums to max of nums.
# For each middle, check if number of valid value in nums >= k.
# If yes, it might be the answer, 
# else it is not the answer.
# This problem is similar to koko eating banana problem.

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        lo, hi = min(nums), max(nums)

        def check(num):
            cnt = 0
            i = 0
            while i < len(nums):
                if nums[i] <= num:
                    cnt += 1
                    i += 1
                i += 1
            
            return cnt >= k


        while lo < hi:
            m = (lo + hi) // 2
            if check(m):
                hi = m
            else:
                lo = m + 1
            
        return lo
    
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        lo, hi = min(nums), max(nums)

        def check(num):
            cnt = 0
            i = 0
            can_steal = True
            for i in nums:
                if can_steal:
                    if i <= num:
                        cnt += 1
                        can_steal = False
                else:
                    can_steal = True

            return cnt >= k


        while lo < hi:
            m = (lo + hi) // 2
            if check(m):
                hi = m
            else:
                lo = m + 1
            
        return lo