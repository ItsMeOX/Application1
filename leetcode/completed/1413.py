from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val = 0
        cur_sum = 0
        for num in nums:
            cur_sum += num
            min_val = min(min_val, cur_sum)
        
        return 1 - min_val
    
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        lo, hi = 1, 10000

        def largerThanZero(n):
            for num in nums:
                n += num
                if n < 1:
                    return False
            return True

        while lo < hi:
            m = (lo + hi) // 2
            if largerThanZero(m):
                hi = m
            else:
                lo = m + 1
        
        return lo
    

sol = Solution()
print(sol.minStartValue([-3,2,-3,4,2]))