from typing import List

# For every index i, we can choose to change nums[i] to 1 ~ 3, and nums[i+1 ~ last] must be >= that chose number.
# If the choice is not equal to current nums[i], then we have to add 1 to res.

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        dpb = [0] * 4
        for i in range(len(nums)-1, -1, -1):
            dpf = [float('inf')] * 4
            for cur_min in range(1, 4):
                for choice in range(cur_min, 4):
                    dpf[cur_min] = min(dpf[cur_min], dpb[choice] + (choice != nums[i]))
            dpb = dpf

        return dpb[1]


        # @cache
        # def dfs(i, cur_min):
        #     if i == len(nums):
        #         return 0
            
        #     res = float('inf')
        #     for choice in range(cur_min, 4):
        #         res = min(res, dfs(i+1, choice) + (choice != nums[i]))
            
        #     return res
        

        # return dfs(0, 1)