from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        k_used = 0
        res = 0

        for right in range(len(nums)):
            if nums[right]:
                res = max(res, right - left + 1)
            else:
                if k_used < k:
                    k_used += 1
                else:
                    while nums[left] == 1:
                        left += 1
                    left += 1

        return max(res, right - left + 1)
    
sol = Solution()              
print(sol.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))