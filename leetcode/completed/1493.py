from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        intervals = []

        cnt = 0
        for i, num in enumerate(nums):
            if num == 0:
                intervals.append(cnt)
                cnt = 0
            else:
                cnt += 1
        intervals.append(cnt)    

        if len(intervals) == 1:
            return len(nums) - 1

        res = 0
        for i in range(1, len(intervals)):
            res = max(res, intervals[i]+intervals[i-1])

        return res
    
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        left = 0
        firstZero = -1

        for right, num in enumerate(nums):
            if num == 0:
                if firstZero != -1:
                    res = max(res, right - left - 1)
                    left = firstZero + 1
                firstZero = right
        res = max(res, right - left)

        if firstZero == -1:
            return len(nums) - 1
        return res
        
sol = Solution()
print(sol.longestSubarray([0,1,1,1,0,1,1,0,1]))