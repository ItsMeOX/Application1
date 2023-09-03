from typing import List

# Keep filling up cups using the top 2 water that has the most amount.
# If one amount of water is 0, then we must use the time equal to the most amount.

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        res = 0
        amount.sort()

        while amount[0]:
            amount[2] -= 1
            amount[1] -= 1
            res += 1
            amount.sort()

        return res + amount[2]