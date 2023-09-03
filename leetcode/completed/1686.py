from typing import List

# For each round, Alice & Bob will choose the stone which the sum of aliceValues and bobValues are highest,
# because it will increase their score at largest scale or decrease opponent's score at largest scale.
# So just greedily choose the highest summed valued stone every round.

class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        sums = [(aliceValues[i]+bobValues[i], aliceValues[i]) for i in range(len(aliceValues))]
        sums.sort(reverse = True)

        res = 0
        for i in range(len(aliceValues)):
            if i & 1:
                res -= sums[i][0] - sums[i][1]
            else:
                res += sums[i][1]
        
        if res > 0:
            return 1
        elif res < 0:
            return -1
        else:
            return 0