class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        right = 0
        while nums[right] not in d:
            d[target - nums[right]] = right
            right += 1
        return [right, d[nums[right]]]

        


sol = Solution()
nums = [150,24,79,50,88,345,3]
print(sol.twoSum(nums, 200))


