from typing import List

# For every queries,
# The earliest day possible = sum(candiesCount[0] ~ candiesCount[i-1]) / cap
# The latest day possible = sum(candiesCount[0] ~ candiesCount[i]) - 1
# (-1 because of 0-indexed)
# Then we just have to check if earliest day <= fav day <= latest day.

class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        prefix = [0]
        for i in range(len(candiesCount)):
            prefix.append(prefix[-1]+candiesCount[i])

        res = []
        for fav_type, fav_day, cap in queries:
            earliest = prefix[fav_type] // cap
            latest = prefix[fav_type+1]-1
            res.append(earliest <= fav_day <= latest)

        return res
