from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        memo = {}
        res = 0
        left = 0
        current_sum = 0

        for right, num in enumerate(nums):
            if num in memo:
                while left <= memo[num]:
                    current_sum -= nums[left]
                    left += 1

            memo[num] = right
            current_sum += num

            res = max(res, current_sum)


        return res
    
    
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        memo = set()
        res = 0
        left = 0
        current_sum = 0

        for right, num in enumerate(nums):
            while num in memo:
                current_sum -= nums[left]
                memo.remove(nums[left])
                left += 1

            memo.add(nums[right])
            current_sum += num

            res = max(res, current_sum)

        return res