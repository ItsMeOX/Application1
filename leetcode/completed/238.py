from collections import deque
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = deque()
        l = len(nums)
        res = []

        cumulative = 1
        for i in range(l-1, -1, -1):
            cumulative *= nums[i] 
            suffix.appendleft(cumulative)
        suffix.append(1)

        cumulative = 1
        for i in range(l):
            res.append(cumulative * suffix[i+1])
            cumulative *= nums[i]
        
        return res
    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1] * l

        cumulative = 1
        for i in range(l):
            res[i] *= cumulative
            cumulative *= nums[i]

        cumulative = 1
        for i in range(l-1, -1, -1):
            res[i] *= cumulative
            cumulative *= nums[i]

        return res

sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))