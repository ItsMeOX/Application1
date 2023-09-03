from typing import List

# Consider following example:
# 0, 2, 1, 0
# We can do a binary search where lo and hi both stop at the first index where arr[mid] > arr[mid+1].
# Here we can set lower bound to 1 as arr[0] will never be the answer,
# we can also set higher bound to second last index as last element will not be the answer.

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo, hi = 1, len(arr)-1
        while lo < hi:
            m = (lo+hi) // 2
            if arr[m+1] < arr[m]:
                hi = m
            else:
                lo = m + 1
        
        return lo