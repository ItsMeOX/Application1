class Solution:
    def canJump(self, nums: list[int]) -> bool:
        furthest = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if furthest - i <= nums[i]:
                furthest = i
                nums[i] = "T"
        return nums[0] == "T"

nums = [0]

sol = Solution()
print(sol.canJump(nums))