from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        inc, dec = 1, 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc = dec + 1
            elif nums[i] < nums[i-1]:
                dec = inc + 1
        
        return max(inc, dec)



sol = Solution()
print(sol.wiggleMaxLength([3,3]))