from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        counter = {}
        cnt = 0

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for i in range(max(nums), 0, -1):
            if i in counter:
                cnt += counter[i]
            
            if i == cnt:
                return i

        return -1
    
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        lo, hi = 0, 101

        while lo < hi:
            m = (lo+hi) // 2

            cnt = 0
            for num in nums:
                if num >= m:
                    cnt += 1
            
            if cnt == m:
                return m
            
            if cnt < m:
                hi = m
            else:
                lo = m + 1

        return -1