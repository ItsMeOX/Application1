from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]

        def dfs(i, current):
            if i == len(nums):
                return
            
            current.append(nums[i])
            if current not in res:
                res.append(list(current))
            for j in range(i+1, len(nums)):
                dfs(j, current)
            current.pop()

        for i in range(len(nums)):
            dfs(i, [])

        return res

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(i, current):
            if i == len(nums):
                res.append(list(current))
                return

            current.append(nums[i])
            dfs(i+1, current)
            current.pop()

            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
            
            dfs(i+1, current)

        dfs(0, [])

        return res