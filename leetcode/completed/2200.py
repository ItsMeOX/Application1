from collections import deque
from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        q = deque()
        res = []

        for i in range(len(nums)):
            if nums[i] == key:
                q.append(i)

        for i in range(len(nums)):
            while q and q[0] < i - k:
                q.popleft()
            
            if q and abs(i - q[0]) <= k:
                res.append(i)
        
        return res