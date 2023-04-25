class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        arrlen = len(nums)
        left = 0
        right = arrlen - 1
        ans = [0] * arrlen

        for i in range(right, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                ans[i] = nums[left] ** 2
                left += 1
            else:
                ans[i] = nums[right] ** 2
                right -= 1
        return ans


sol = Solution()
print(sol.sortedSquares([-7,-5,-3,0,2,5,6,7,8]))