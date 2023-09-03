from typing import List
from heapq import heappush, heappop

# Unoptimized, T: O(nlogn), M: O(n)

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        heap = []
        counter = {}

        for num in nums:
            if num not in counter:
                heappush(heap, num)
                counter[num] = 0
            counter[num] += 1
    
        cur_max = 0
        for i, num in enumerate(nums):
            cur_max = max(cur_max, num)
            counter[num] -= 1
            if not counter[num]:
                del counter[num]
            while heap[0] not in counter:
                heappop(heap)
            if heap[0] >= cur_max:
                return i+1
            
# Consider a array: [1,1,1,0,6,12]
# To partition array which all elms in left subarray are <= all elms in right subarray,
# We need to find the point where
# the maximum of left subarray is <= minimum of right subarray.
# [ 1,1,1,0 | 6,12  ]
#   max: 1  | min: 6

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        right_min = [0] * n
        right_min[-1] = nums[-1]
        left_max = nums[0]

        for i in range(n-2, -1, -1):
            right_min[i] = min(right_min[i+1], nums[i])
        
        for i in range(n-1):
            left_max = max(left_max, nums[i])
            if right_min[i+1] >= left_max:
                return i + 1