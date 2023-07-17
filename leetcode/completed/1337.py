from heapq import heappop, heappush
from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []

        for i in range(len(mat)):
            cur_row = mat[i]
            heappush(heap, (cur_row.count(1), i))
        
        res = []
        for _ in range(k):
            _, i = heappop(heap)
            res.append(i)

        return res