from typing import List

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        larger = 0
        cur_k = 0
        for smaller in range(1, len(arr)):
            if arr[smaller] > arr[larger]:
                cur_k = 1
                larger = smaller
            else:
                cur_k += 1
            
            if cur_k == k:
                return arr[larger]
        
        return arr[larger]