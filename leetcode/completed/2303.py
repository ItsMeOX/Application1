from typing import List

# Using two pointers here,
# [1]         -> [1]
# [1,2]       -> [2], [1,2]
# [1,2,3]     -> [3], [2,3], [1,2,3]
# [1,2,3,4]   -> [4], [3,4], [2,3,4], [1,2,3,4]
# [1,2,3,4,5] -> [5], [4,5], [3,4,5], [2,3,4,5], [1,2,3,4,5]
# Every time we move right pointer to right + 1, there will be right - left + 1 new subarrays.
# Every time cur_sum is >= k, we will adjust our window by incrementing left pointer to left+1.

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        cur_sum = 0
        res = 0

        for right in range(len(nums)):
            cur_sum += nums[right]
            while cur_sum * (right - left + 1) >= k:
                cur_sum -= nums[left]
                left += 1
            
            res += right - left + 1
        
        return res