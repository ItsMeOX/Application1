from typing import List
from heapq import heappush, heappop

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        heap2 = []
        n = len(nums1)

        nums1.sort(reverse=True)

        for i in range(n):
            heappush(heap2, (-nums2[i], i))

        res = [0] * n
        for i in range(n):
            val, idx = heappop(heap2)
            while -val >= nums1[i]:
                heappush(heap2, (1, idx))
                val, idx = heappop(heap2)

            res[idx] = nums1[i]

        return res