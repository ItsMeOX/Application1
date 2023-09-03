from heapq import heappop, heappush
from typing import List

# Greedily subtract sum of 'nums' by half of current largest number until sum is <= original_sum / 2.

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        sums = sum(nums)
        target = sums / 2
        heap = []
        res = 0

        for num in nums:
            heappush(heap, -num)

        while sums > target:
            num = -heappop(heap)
            num /= 2
            sums -= num
            heappush(heap, -num)
            res += 1

        return res