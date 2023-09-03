from typing import List

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:

        seen1 = set(nums1)
        seen2 = set(nums2)
        seen3 = set(nums3)
        res = set()

        for s1 in seen1:
            if s1 in seen2 or s1 in seen3:
                res.add(s1)
        
        for s2 in seen2:
            if s2 in seen1 or s2 in seen3:
                res.add(s2)

        for s3 in seen3:
            if s3 in seen1 or s3 in seen2:
                res.add(s3)

        return res
    
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        seen1 = set(nums1)
        seen2 = set(nums2)
        seen3 = set(nums3)

        return (seen1 & seen2) | (seen1 & seen3) | (seen2 & seen3)