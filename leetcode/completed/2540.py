from typing import List
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        left = right = 0
        n1, n2 = len(nums1), len(nums2)

        while left < n1 and right < n2:
            if nums1[left] < nums2[right]:
                left += 1
            elif nums1[left] > nums2[right]:
                right += 1
            else:
                return nums1[left]

        return -1