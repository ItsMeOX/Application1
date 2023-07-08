from typing import List
from heapq import heappop, heappush

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        leftHeap = []
        rightHeap = []

        l = 0
        r = len(costs)-1

        for _ in range(candidates):
            if l == r:
                heappush(leftHeap, costs[l])
                l += 1
                break
            if r < l:
                break
            heappush(leftHeap, costs[l])
            heappush(rightHeap, costs[r])
            l += 1
            r -= 1

        res = 0

        leftCost = heappop(leftHeap) if leftHeap else float('inf')
        rightCost = heappop(rightHeap) if rightHeap else float('inf')

        for _ in range(k):
            if leftCost <= rightCost:
                res += leftCost
                if l <= r:
                    heappush(leftHeap, costs[l])
                    l += 1
                if leftHeap:
                    leftCost = heappop(leftHeap)
                else:
                    leftCost = float('inf')
            else:
                res += rightCost
                if l <= r:
                    heappush(rightHeap, costs[r])
                    r -= 1
                if rightHeap:
                    rightCost = heappop(rightHeap)
                else:
                    rightCost = float('inf')

        return res


sol = Solution()
print(sol.totalCost([17,12,10,2,7,2,11,20,8]
, 3, 4))