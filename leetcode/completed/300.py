class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)-2, -1, -1):
            temp = 0
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    temp = max(temp, dp[j])

            dp[i] += temp
            print(dp)

        return max(dp)

from random import randint
matrix = [1,3,5,4,7]
sol = Solution()
print(sol.lengthOfLIS(matrix))