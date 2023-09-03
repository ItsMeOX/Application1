from typing import List

# Sort the array and add current smallest and largest elements to 'res' array alternatively.

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        
        for i in range(len(nums)//2+(len(nums)&1)):
            res.append(nums[i])
            res.append(nums[len(nums)-i-1])
        
        if len(nums)&1: res.pop()

        return res

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        
        for i in range(0, len(nums)-1, 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]

        return nums