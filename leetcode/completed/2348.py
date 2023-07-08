from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zeroes = 0
        res = 0

        for num in nums:
            if num == 0:
                zeroes += 1
            else:
                res += zeroes*(zeroes+1)//2
                zeroes = 0

        return res + zeroes*(zeroes+1)//2 if zeroes else res