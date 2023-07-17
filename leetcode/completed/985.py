from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total_sum = 0
        res = []

        for num in nums:
            if not num & 1:
                total_sum += num
        
        for val, i in queries:
            if not nums[i] & 1:
                total_sum -= nums[i]
            
            nums[i] += val

            if not nums[i] & 1:
                total_sum += nums[i]

            res.append(total_sum)

        return res