from typing import List
from heapq import heapify, heappop, heappush

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapify(nums)
        self.length = len(nums)

        while self.length > k:
            heappop(self.heap)
            self.length -= 1

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        self.length += 1
        if self.length > self.k:
            heappop(self.heap)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)