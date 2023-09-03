from typing import List

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)-1):
            cur_sum = nums[i] + nums[i+1]
            if cur_sum in seen: return True
            seen.add(cur_sum)
        
        return False