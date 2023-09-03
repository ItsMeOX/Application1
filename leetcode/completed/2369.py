from typing import List

# Here from i = 0 we check if 
# 1. nums[i] == nums[i+1]                  , if yes then go to i + 2,
# 2. nums[i] == nums[i+1] == nums[i+2]     , if yes then go to i + 3,
# 3. nums[i] == nums[i+1]-1 == nums[i+2]-2 , if yes then go to i + 3,
# if we ever reach len(nums), that means there is a valid partition, so just return True all the way to base call.
# Else, after False is returned, we mark the cell as visited and next time we visited this cell,
# we will know that this cell is invalid so just return False.

class Solution:
    def validPartition(self, nums: List[int]) -> bool:

        visited = set()

        def dfs(i):
            if i == len(nums):
                return True
            
            if i in visited:
                return False

            # two equal
            if i + 1 < len(nums) and nums[i] == nums[i+1]:
                if dfs(i+2):
                    return True

            # three equal & three consecutive
            if i + 2 < len(nums): 
                if nums[i] == nums[i+1] == nums[i+2] or nums[i] == nums[i+1]-1 == nums[i+2]-2:
                    if dfs(i+3):
                        return True
            
            visited.add(i)

            return False

        return dfs(0)