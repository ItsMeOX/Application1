from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []

        idx = bisect_left(arr, x)
        if idx == len(arr):
            idx -= 1        
        elif idx and abs(arr[idx-1]-x) <= abs(arr[idx]-x):
            idx -= 1
        res.append(arr[idx])

        k -= 1

        left = right = 1
        while k > 0:
            if idx - left < 0:
                res.append(arr[idx+right])
                right += 1
            elif idx + right >= len(arr):
                res.append(arr[idx-left])
                left += 1
            elif x-arr[idx-left] <= arr[idx+right]-x:
                res.append(arr[idx-left])
                left += 1
            else:
                res.append(arr[idx+right])
                right += 1
            k -= 1

        return sorted(res)

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr)-1

        while right-left+1 > k:
            if abs(arr[left]-x) > abs(arr[right]-x):
                left += 1
            else:
                right -= 1
        
        return arr[left:right+1]
    
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k

        while left < right:
            m = (left+right) // 2
            if x-arr[m] > arr[m+k]-x:
                left = m + 1
            else:
                right = m
        
        return arr[left: left+k]

sol = Solution()
print(sol.findClosestElements([1,1,2,2,2,2,2,3,3],3,3))