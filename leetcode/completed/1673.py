from typing import List

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        res = []

        for i, num in enumerate(nums):
            while res and res[-1] > num and (len(nums)-i)+len(res)>k:
                res.pop()
            if len(res) < k:
                res.append(num)
        
        return res