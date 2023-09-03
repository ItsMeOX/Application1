from typing import List

# Brute force solution:
# Create a prefix sum of nums.
# Iterate from firstLen to n+1, current sum for firstLen 'first_sum' = prefix[i] - prefix[i-firstLen]
# For every iteration of firstLen, iterate from secondLen to n+1.
# Consider following intervals:
# [0,1,2,3,4,5] 
# if firstLen = 1 and i = 2, interval of current i will then be (i-firstLen,i] = (1, 2] => [2]. 
# if secondLen = 1 and j = 3, interval for current j will be (j-secondLen, j] = (2, 3]  => [3].
# if secondLen = 1 and j = 1, interval for current j will be (j-secondLen, j] = (0, 1]  => [1].
# So, for the two to not overlap, the condition will be j-secondLen >= i or j <= i-firstLen.

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        prefix = [0] * (n+1)
        res = 0

        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + nums[i-1]
        
        for i in range(firstLen, n+1):
            first_sum = prefix[i] - prefix[i-firstLen]
            for j in range(secondLen, n+1):
                if j-secondLen >= i or j <= i-firstLen:
                    res = max(res, first_sum + prefix[j]-prefix[j-secondLen])
        
        return res

# Optimization:
# Initialize a prefix sum.
# We have 3 variables: 
# 'res': maximum sum between two subarrays.
# 'left_max': maximum sum of left subarray.
# 'right_max': maximum sum of right subarray.
# Sliding window technique is used here.
# First, we initialize two windows |---firstLen---||---secondLen---|,
# then we move both of the windows right together but if the left window has obtained its maximum sum then stop sliding it 
# (by keeping 'left_max' always the maximum left subarray sum).
# For every iteration, we update 'res' with (maximum left subarray sum + current right window sum) if 'res' has lower value.
# Then, we also do the same thing the second time but this time swapping the length of the windows |---secondLen---||---firstLen---|.


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        prefix = [0] * (n+1)

        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + nums[i-1]

        res = 0
        left_max = 0
        right_max = 0

        for i in range(firstLen+secondLen, n+1):
            left_max = max(left_max, prefix[i - secondLen] - prefix[i - firstLen - secondLen])
            res = max(res, left_max + prefix[i] - prefix[i - secondLen])

        for i in range(firstLen+secondLen, n+1):
            right_max = max(right_max, prefix[i - firstLen] - prefix[i - firstLen - secondLen])
            res = max(res, right_max + prefix[i] - prefix[i- firstLen])
        
        return res

sol = Solution()
print(sol.maxSumTwoNoOverlap(nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2))