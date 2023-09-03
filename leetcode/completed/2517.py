from typing import List

# Use binary search to search from 0 to max(price).
# Here m will be the minimum difference of prices of any two candies,
# we will greedily find how many prices satifies difference >= m.
# If amount of prices >= m, we can try to higher up m,
# else we should lower down m.

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()

        def check(target):
            prev = price[0]
            res = 1
            for p in price:
                if p - prev >= target:
                    prev = p
                    res += 1
            
            return res
        
        lo, hi = 0, price[-1]

        while lo < hi:
            m = (lo+hi) // 2
            if check(m) >= k:
                lo = m + 1
            else:
                hi = m
        
        return lo - 1