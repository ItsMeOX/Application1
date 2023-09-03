from typing import List

# Sort each row of the matrix,
# then find the max for each column and sum them up.

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for num in nums:
            num.sort()

        res = 0
        for col in zip(*nums):
            res += max(col)

        return res