from heapq import heappop, heappush
from typing import List

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []

        for p in piles:
            heappush(heap, -p)
        
        for _ in range(k):
            heappush(heap, heappop(heap)//2)

        return -sum(heap)