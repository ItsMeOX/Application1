from typing import List

# Count function:
# check how many balls can be placed where the distance between two adjacent balls
# is >= distance.
# If count >= m, then we can place more balls, so lo = m + 1,
# if count <  m, then the distance is too large, so hi = m.

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def count(distance):
            res = 1
            left = position[0]

            for right in position:
                if right - left >= distance:
                    res += 1
                    left = right
            
            return res
        
        lo, hi = 0, max(position)
        while lo < hi:
            mi = (lo+hi) // 2
            if count(mi) >= m:
                lo = mi + 1
            else:
                hi = mi

        return lo - 1