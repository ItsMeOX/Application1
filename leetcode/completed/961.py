from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

# As the most appeared number occupies length / 2 space,
# we just have to check nums[i+1] or nums[i+2] or nums[i+3] is same with nums[i] == 1 or not.
# for n = 2,
# [a, a, b, c]
# [a, b, a, c]
# [a, b, c, a]

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i+1] == nums[i]:
                return nums[i]
            
            if i+2 < len(nums) and nums[i+2] == nums[i]:
                return nums[i]

            if i+3 < len(nums) and nums[i+3] == nums[i]:
                return nums[i]