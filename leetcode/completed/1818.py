from typing import List
from bisect import bisect_left

# Calculate the sum of absolute difference between nums1 and nums2 first.
# Then sort nums1 in increasing order, 'ref' here.
# For each index i from 0 ~ len(nums1), we binary search for the number in nums1 that is closest to nums2[i] from array 'ref'.
# Then we compare if ref[i] or ref[i-1] is closer to nums2[i].
# ( Remember to handle case like i = 0 or i = len(ref) )

# For example:

# sorted(nums1): [1,5,7,9,10], nums2[i]: 4,
# binary searched 'idx' will be 1, and we will compare 1 and 5 and choose 5.

# sorted(nums1): [1,5,7,9,10], nums2[i]: 5,
# 'idx' will be 1, we will compare 1 and 5 and choose 5.

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        sums = 0
        MOD = 10 ** 9 + 7
        ref = sorted(set(nums1))

        for i in range(len(nums1)):
            sums += abs(nums1[i] - nums2[i])

        res = sums
        for i in range(len(nums1)):
            cur_diff = abs(nums1[i] - nums2[i])
            idx = bisect_left(ref, nums2[i])
            if idx>0       : res = min(res, sums - cur_diff + abs(ref[idx-1] - nums2[i])) # sums - diff added at first loop + current diff
            if idx<len(ref): res = min(res, sums - cur_diff + abs(ref[idx]   - nums2[i]))

        return res % MOD
    
# Here instead of using set,
# we can skip right to the last duplicated number of 'ref' by using bisect_right.
# For example:
# nums1 = [1,2,2,2,3]
# bisect_right(2) = 4, and we will compare index 4 and 3.

from bisect import bisect_right
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        sums = 0
        MOD = 10 ** 9 + 7
        ref = sorted(nums1)

        for i in range(len(nums1)):
            sums += abs(nums1[i] - nums2[i])

        res = sums
        for i in range(len(nums1)):
            cur_diff = abs(nums1[i] - nums2[i])
            idx = bisect_right(ref, nums2[i])
            if idx>0       : res = min(res, sums - cur_diff + abs(ref[idx-1] - nums2[i]))
            if idx<len(ref): res = min(res, sums - cur_diff + abs(ref[idx] - nums2[i]))

        return res % MOD