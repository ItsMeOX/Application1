from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda e: (bin(e).count('1'), e))
    
from heapq import heappop, heappush
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        temp = []
        res = []

        def countOne(num):
            one = 0
            while num:
                one += num & 1
                num >>= 1
            return one

        for num in arr:
            heappush(temp, (countOne(num), num))

        while temp:
            res.append(heappop(temp)[1])
        
        return res