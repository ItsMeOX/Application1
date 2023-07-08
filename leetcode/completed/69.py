class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1

        lo, hi = 0, x//2

        while lo <= hi:
            m = (lo+hi) // 2
            if m * m > x:
                hi = m - 1
            else:
                lo = m + 1
        
        return lo - 1

class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x

        while lo <= hi:
            m = (lo+hi) // 2
            if m * m == x:
                return m
            elif m * m > x:
                hi = m - 1
            else:
                lo = m + 1
        
        return lo - 1
