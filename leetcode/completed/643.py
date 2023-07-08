from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = -float('inf')
        c = 0
        for i in range(k):
            c += nums[i]

        for i in range(k, len(nums)):
            res = max(res, c / k)
            c -= nums[i-k]
            c += nums[i]

        res = max(res, c / k)

        return res
    
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = 0
        for i in range(k):
            max_sum += nums[i]
        temp = max_sum

        for i in range(len(nums)-k):
            temp = temp - nums[i] + nums[i+k]
            max_sum = max(max_sum, temp)

        return max_sum / k