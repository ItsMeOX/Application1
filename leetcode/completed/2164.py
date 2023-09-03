from typing import List

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = []
        odds = []

        for i in range(len(nums)):
            if i & 1: odds.append(nums[i])
            else: even.append(nums[i])
        
        even.sort()
        odds.sort(reverse=True)
        res = []

        for i in range(len(even)):
            res.append(even[i])
            if i < len(odds):
                res.append(odds[i])
        
        return res