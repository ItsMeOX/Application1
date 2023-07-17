from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # 15 4 4 4 4  (16)
        # 8 15 4 4
        total_sum = sum(nums)
        if total_sum < x:
            return -1
        if total_sum == x:
            return len(nums)

        target = total_sum - x
        cur_sum = 0
        left = 0
        longest = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            
            while cur_sum > target:
                cur_sum -= nums[left]
                left += 1

            if cur_sum == target:
                longest = max(longest, i - left + 1)
        
        if longest == 0:
            return -1
        return len(nums) - longest


sol = Solution()
print(sol.minOperations([3,2,20,1,1,3], x = 10))