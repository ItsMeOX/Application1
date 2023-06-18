class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        _min = nums[0]
        res = 0
        for i in range(len(nums)-1):
            _min = min(_min, nums[i])
            res = max(res, nums[i+1]-_min)

        return res if res else -1