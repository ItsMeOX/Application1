class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        
        _min = nums[0]
        res = 0
        for num in nums:
            if num > _min and num - _min > k:
                res += 1
                _min = num

        return res + 1



sol = Solution()
print(sol.partitionArray(nums = [3,1,3,4,2], k = 0))