class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for x in nums:
            if nums[left] != x:
                left += 1
                nums[left] = x
        
        return left + 1