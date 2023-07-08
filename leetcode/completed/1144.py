from typing import List

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        # make all odds smaller than neigbour values
        temp_odd = 0
        for i in range(1, len(nums), 2):
            if i == len(nums)-1:
                if nums[i] >= nums[i-1]:
                    temp_odd += nums[i] - nums[i-1] + 1
            else:
                nei_min = min(nums[i-1], nums[i+1])
                if nums[i] >= nei_min:
                    temp_odd += nums[i] - nei_min + 1
        
        # make all even smaller than neigbour values
        temp_even = 0
        for i in range(0, len(nums), 2):
            if i == 0:
                if nums[i] >= nums[i+1]:
                    temp_even += nums[i] - nums[i+1] + 1
            elif i == len(nums)-1:
                if nums[i] >= nums[i-1]:
                    temp_even += nums[i] - nums[i-1] + 1
            else:
                nei_min = min(nums[i-1], nums[i+1])
                if nums[i] >= nei_min:
                    temp_even += nums[i] - nei_min + 1

        return min(temp_even, temp_odd)
    
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        nums = [float('inf')] + nums + [float('inf')]

        res = [0, 0]
        for i in range(1, len(nums)-1):
            res[i%2] += max(0, nums[i] - min(nums[i-1], nums[i+1]) + 1)

        return min(res)