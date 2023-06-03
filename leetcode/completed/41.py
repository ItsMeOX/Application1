class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        min_num = float('inf')
        for i in range(len(nums)):
            if nums[i] > 0:
                if nums[i] < min_num:
                    min_num = nums[i]
            else:
                nums[i] = len(nums) + 1

        if min_num != 1:
            return 1
        
        for num in nums:
            if abs(num) <= len(nums) and nums[abs(num)-1] > 0:
                nums[abs(num)-1] = -nums[abs(num)-1]

        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1
            
        return len(nums)+1


sol = Solution()
print(sol.firstMissingPositive([1]))