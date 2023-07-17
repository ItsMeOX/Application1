from typing import List
from collections import defaultdict

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        k = k1 + k2

        difference_list = [abs(num1-num2) for num1, num2 in zip(nums1, nums2)]

        differences = defaultdict(int)
        for d in difference_list:
            differences[d] += 1

        max_key = max(differences.keys())

        for key in range(max_key, 0, -1):
            if key in differences:
                temp = min(k, differences[key])
                differences[key-1] += temp
                differences[key] -= temp
                k -= temp
        
        res = 0
        for key, val in differences.items():
            res += key ** 2 * val

        return res





# 1 - 5  -> 4 16/9
# 4 - 8  -> 4 16/9
# 10 - 6 -> 4 16/9
# 12 - 9 -> 3 9/

from heapq import heappush, heappop 
class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int: # TLE
        k = k1 + k2

        difference = []

        for num1, num2 in zip(nums1, nums2):
            heappush(difference, -abs(num1-num2))

        for _ in range(k):
            if difference[0] == 0:
                break
            cur_max = heappop(difference)
            heappush(difference, cur_max + 1)
        
        res = 0
        for d in difference:
            res += d ** 2

        return res

