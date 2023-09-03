from typing import List

# O(len(nums1) + len(nums2))

# We have left and right pointers.
# Iterate through nums1 by moving left pointer 1 each iteration.
# For each iteration, we move right pointer until nums2[right+1] < nums1[left].
# If right pointer reached last element of nums2, then do not move it anymore.
# We also update res if right - left is larger res every iteration.

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        right = 0
        res = 0

        for left in range(len(nums1)):
            while right < len(nums2)-1 and nums2[right+1] >= nums1[left]:
                right += 1
            res = max(res, right - left)

        return res

# O(len(nums2) * log(len(nums1)))

# For every iteration of nums2, find the left most number that is <= than nums2[i], 
# then ( i - idx of left most element of nums1 array that is <= nums2[i] ).
# Here we have to make sure that the nums1[idx] is <= nums2[i].
# For example, consider the following nums1 and nums2:
# nums1: [2]
# nums2: [2,2,1]
# when i = 2, idx will be 0, which is not valid as nums1[idx] > nums2[i].

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        def binarySearch(target):
            lo, hi = 0, len(nums1)-1
            while lo < hi:
                m = (lo+hi) // 2
                if nums1[m] <= target:
                    hi = m
                else:
                    lo = m + 1
            return lo

        res = 0
        for i in range(len(nums2)):
            idx = binarySearch(nums2[i])
            if nums1[idx] <= nums2[i]:
                res = max(res, i - idx)

        return res