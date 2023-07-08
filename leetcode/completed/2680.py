from typing import List

class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        prefix = [0] + [num for num in nums]
        
        suffix = [num for num in nums] + [0]

        for num in range(1, n+1):
            prefix[num] = nums[num-1] | prefix[num-1] 

        for num in range(n-1, -1, -1):
            suffix[num] = nums[num] | suffix[num+1]

        res = 0
        for num in range(n):
            temp = (nums[num] << k) | prefix[num] | suffix[num+1]
            res = max(res, temp)

        return res

sol = Solution()
print(sol.maximumOr([8,3,6,2,1], 5))