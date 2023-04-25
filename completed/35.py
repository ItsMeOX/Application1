class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        middle = 0

        while (left <= right):
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle

        print(left)
        if nums[middle] > target:
            return middle
        else:
            return middle + 1
            

sol = Solution()
print(sol.searchInsert([0,1,3,4,5,6,7,8], 2))