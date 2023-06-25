from typing import List
from math import ceil
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        lo, hi = 1, max(quantities)

        def check(number):
            n_needed = 0
            for q in quantities:
                n_needed += ceil(q/number)

            if n_needed > n:
                return False
            return True 

        while lo <= hi:
            m = (lo+hi) // 2
            if check(m):
                hi = m - 1
            else:
                lo = m + 1

        return lo

sol = Solution()
print(sol.minimizedMaximum(n = 7, quantities = [15,10,10]))