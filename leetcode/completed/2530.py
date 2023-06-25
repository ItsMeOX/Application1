from typing import List
import heapq
from math import ceil

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        res = 0
        for _ in range(k):
            largest = heapq.heappop(nums) 
            res += -largest
            heapq.heappush(nums, -ceil(-largest / 3))

        return res