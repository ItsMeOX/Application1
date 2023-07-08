from typing import List
from heapq import heappop, heappush

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_heap = []
        max_heap = []
        res = 0
        left = 0

        for i , num in enumerate(nums):
            heappush(min_heap, (num, i))
            heappush(max_heap, (-num, i))

            while min_heap[0][1] < left:
                heappop(min_heap)
            while max_heap[0][1] < left:
                heappop(max_heap)

            if -max_heap[0][0]-min_heap[0][0] > limit:
                left += 1
            else:
                res = max(res, i - left + 1)

        return res