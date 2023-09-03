from typing import List

# For every rung, if (rung - prev rung) <= dist, we do nothing.
# Else, we need to calculate how many rungs to insert between.
# We can do this by (rung - prev - 1) / dist,
# we -1 here because that if rung - prev == dist, we will not need to add rung.
# So -1 can fix this.

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        res = 0
        prev = 0

        for rung in rungs:
            if rung - prev > dist:
                res += (rung - prev - 1) // dist
            prev = rung
        
        return res
