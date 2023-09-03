from typing import List
from bisect import bisect_right

# Because that it wants subsequence not subarray, so we can sort the nums.
# Iterate i from 0 to len(nums), 
# for every nums[i], we find j, the index which nums[i] + nums[j] <= target.
# Then for example if our array is like: 
# [1,2,2,3,4,5], target = 6
# we can calculate the number of subsequences as below:
# 1. we must take '1' or else the sum of pair will excceed target.
# 2. if we have taken '1', then we have 5 elements left, and we can either 'choose' or 'not choose' it,
#    so the number of subsequences will be 
#    = 2 ** (len(subarray) - 1)
#    = 2 ** (j - i)
# Note that if j < i then we have to skip current iteration.

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        MOD = 10 ** 9 + 7

        for i in range(len(nums)):
            j = bisect_right(nums, target - nums[i]) - 1
            if j < i: continue
            res += 2 ** (j-i) # 2 << (j-1) will run much faster

        return res % MOD
    
# not so clear solution
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        MOD = 10 ** 9 + 7

        left, right = 0, len(nums)-1 

        while left <= right:
            if nums[left] + nums[right] <= target:
                res += 1 << (right - left)
                left += 1
            else:
                right -= 1

        return res % MOD