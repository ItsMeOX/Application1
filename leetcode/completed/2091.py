from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_i = 0
        max_i = 0
        n = len(nums)

        for i in range(n):
            if nums[i] < nums[min_i]:
                min_i = i
            if nums[i] > nums[max_i]:
                max_i = i

        return min(
            max(min_i, max_i)+1,
            n-min(min_i, max_i),
            min(min_i, max_i)+1 + n-max(min_i, max_i)
        )
    

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_i = 0
        max_i = 0
        n = len(nums)

        for i in range(n):
            if nums[i] < nums[min_i]:
                min_i = i
            if nums[i] > nums[max_i]:
                max_i = i

        if max_i < min_i:
            max_i, min_i = min_i, max_i

        return min(
            max_i+1,
            n-min_i,
            min_i+1 + n-max_i
        )