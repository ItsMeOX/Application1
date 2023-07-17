from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * (n+1)
        suffix = [0] * (n+1)

        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + nums[i-1]

        for i in range(n-1, -1, -1):
            suffix[i] = suffix[i+1] + nums[i]

        res = []
        for i in range(n):
            res.append(abs(prefix[i]-suffix[i+1]))

        return res
    
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = sum(nums)
        res = []

        for i in range(n):
            left += nums[i]
            res.append(abs(right-left))
            right -= nums[i]

        return res