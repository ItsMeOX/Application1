class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left = 0  
        right = sum(nums)

        for idx,val in enumerate(nums):
            
            right -= val
            if left == right:
                return idx
            left += val

        return -1


sol = Solution()
nums = [2,1,1,1,-1]

print(sol.pivotIndex(nums))