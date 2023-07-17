from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peak = arr.index(max(arr))

        if peak == 0 or peak == len(arr)-1: return False

        for i in range(1, peak+1):
            if arr[i] <= arr[i-1]:
                return False
        
        for i in range(peak+1, len(arr)):
            if arr[i] >= arr[i-1]:
                return False

        return True
    
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)

        left, right = 0, n-1

        while left < n - 1 and arr[left] < arr[left+1]:
            left += 1

        while right > 0 and arr[right-1] > arr[right]:
            right -= 1

        return left != 0 and right != n - 1 and left == right 