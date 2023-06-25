from typing import List
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        maxMultiplier = max(time) * 2 // 60
        
        res = 0

        memo = {}

        for t in time:
            for multiplier in range(1,maxMultiplier + 1):
                if multiplier * 60 - t in memo:
                    res += memo[multiplier * 60 - t]
            memo[t] = memo.get(t, 0) + 1

        return res

from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        memo = defaultdict(int)
        
        for t in time:
            remainder = t % 60
            if remainder == 0:
                res += memo[0]
            else:
                res += memo[60 - remainder]
            memo[remainder] += 1

        return res