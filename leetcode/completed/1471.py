from typing import List

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        
        n = len(arr)
        left = 0
        right = n-1

        res = []

        for _ in range(k):
            if arr[(n-1)//2] - arr[left] > arr[right] - arr[(n-1)//2]:
                res.append(arr[left])
                left += 1
            else:
                res.append(arr[right])
                right -= 1
        return res