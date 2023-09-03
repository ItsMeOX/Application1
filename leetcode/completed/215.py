from typing import List
from heapq import heapify, heappop, heappush

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for num in nums:
            heappush(heap, -num)

        for _ in range(k-1):
            heappop(heap)

        return -heappop(heap)
    

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)

        while len(nums) > k:
            heappop(nums)
        
        return nums[0]
    
# Using count sort here.
# We initialize 'count' list which stores the frequency that every number from min_val to max_val appears.
# We then iterate from last element of 'count' and subtract the frequency from k (here is remain).
# If k is less than or equal to 0, then it will be our answer.
# Time complexity: O(n), Space complexity: O(max(nums)-min(nums))

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_val = min(nums)
        max_val = max(nums)
        count = [0] * (max_val - min_val + 1)

        for num in nums:
            count[num - min_val] += 1

        remain = k
        for i in range(len(count)-1, -1 ,-1):
            remain -= count[i]

            if remain <= 0:
                return i + min_val