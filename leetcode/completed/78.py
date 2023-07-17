from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        temp = []

        def backtrack(i):
            for j in range(i, len(nums)):
                temp.append(nums[j])
                res.append(temp.copy())
                backtrack(j+1)
                temp.pop()
            
        backtrack(0)

        return res