from typing import List

# we only care about the max value of nums[x < i] and min value of nums[x > i]
# precompute max_so_far from left and precompute min_so_far from right
# check at i if max_so_far at i is smaller than nums[i]
# check at i if min_so_far at i is larger  than nums[i]
# if yes -> res + 2
# if no, check if nums[i-1] < nums[i] < nums[i+1]
# if yes -> res + 1

class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]

        for i in range(1, n):
            prefix[i] = max(prefix[i-1], nums[i-1])

        for i in range(n-2, -1, -1):
            suffix[i] = min(suffix[i+1], nums[i+1])

        res = 0
        for i in range(1, n-1):
            if prefix[i] < nums[i] and nums[i] < suffix[i]:
                res += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                res += 1

        return res
    

class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        left = nums[0]
        suffix = [0] * n
        suffix[-1] = nums[-1]

        for i in range(n-2, -1, -1):
            suffix[i] = min(suffix[i+1], nums[i+1])

        res = 0
        for i in range(1, n-1):
            left = max(left, nums[i-1])
            if left < nums[i] and nums[i] < suffix[i]:
                res += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                res += 1

        return res