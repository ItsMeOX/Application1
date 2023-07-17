from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)

        max_num = max(nums)
        max_num_count = nums.count(max_num) * 2
        max_num_encounter_count = 0

        stack = []
        i = 0

        while max_num_encounter_count != max_num_count:
            if nums[i] == max_num:
                max_num_encounter_count += 1

            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)
            
            i += 1
            if i == len(nums): 
                i = 0

        return res
    
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []

        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]

        return res