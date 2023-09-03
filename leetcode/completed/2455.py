from typing import List

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        cnt = sums = 0

        for num in nums:
            if num % 6 == 0:
                cnt += 1
                sums += num
        
        return sums // cnt if cnt else 0