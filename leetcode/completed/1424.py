from typing import List

# TLE
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        max_len = 0

        for i in range(len(nums)):
            r = nums[i]
            if len(r) > max_len:
                max_len = len(r)

        for r in range(len(nums)):
            c = 0
            while r >= 0:
                if len(nums[r]) > c:
                    res.append(nums[r][c])
                r -= 1
                c += 1
        
        for c in range(1, max_len):
            r = len(nums)-1
            while c < max_len and r >= 0:
                if len(nums[r]) > c:
                    res.append(nums[r][c])
                r -= 1
                c += 1
        
        return res
    
# Notice that every elements in same diagonal have same sum(row + col).
# We can group elements that have same sum(row + col) in one array using dictionary.

from heapq import heappush, heappop
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        heap = []

        for r in range(len(nums)):
            for c in range(len(nums[r])):
                heappush(heap, (r+c, c, r))
        
        while heap:
            _, c, r = heappop(heap)
            res.append(nums[r][c])

        return res
    
from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        diagonal = defaultdict(list)

        for r in range(len(nums)):
            for c in range(len(nums[r])):
                diagonal[r+c].append(nums[r][c])
        
        for arr in diagonal.values():
            arr.reverse()
            res.extend(arr)

        return res