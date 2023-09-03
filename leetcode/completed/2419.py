from typing import List

# Any operation of bitwise AND will decrease the number,
# for example 4 & 2 = 100 & 010 = 0.
# So it's best to just not perform any operation of bitwise AND.
# Hence, we can return the longest subarray which the elements in the 
# subarray contains only the maximum number in array.

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = max(nums)
        temp = 0
        res = 0
        for num in nums:
            if num == max_num:
                temp += 1
                res = max(res, temp)
            else:
                temp = 0

        return res