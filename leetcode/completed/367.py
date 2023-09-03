# We want to search for the number which its square is == num.
# Instead of linear search, we can use binary search.
# Binary search from 1 to num,
# if m**2 >= m, hi = m
# else lo = m + 1.


class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        lo, hi = 1, num

        while lo < hi:
            m = (lo+hi) // 2
            if m*m >= num:
                hi = m
            else:
                lo = m + 1
        
        return lo * lo == num