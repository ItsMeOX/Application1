from typing import List
from heapq import heappush, heappop

# Using heap here, explore the current smallest number for k iteration,
# for every heappop, add the bottom and the right grid to heap.

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        heap.append((matrix[0][0], 0, 0))

        while k:
            node, r, c = heappop(heap)
            if matrix[r][c] == -1: continue
            matrix[r][c] = -1
            if r < n-1:
                heappush(heap, (matrix[r+1][c], r+1, c))
            if c < n-1:
                heappush(heap, (matrix[r][c+1], r, c+1))
            k -= 1

        return node
    
# Using binary search here, 
# lower bound = matrix[0][0]
# higher bound = matrix[-1][-1].
# If x elements that are <= m are >= k, then decrease the higher bound,
# else increase the lower bound.

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        lo, hi = matrix[0][0], matrix[-1][-1]

        while lo < hi:
            m = (lo+hi) // 2
            smaller = 0
            for r in range(n):
                ptr = n-1
                while ptr > -1 and matrix[r][ptr] > m:
                    ptr -= 1
                smaller += ptr + 1
            
            if smaller >= k:
                hi = m
            else:
                lo = m + 1
        
        return lo