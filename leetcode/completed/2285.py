from typing import List

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        cntList = {}

        for road in roads:
            a, b = road[0], road[1]
            cntList[a] = cntList.get(a, 0) + 1
            cntList[b] = cntList.get(b, 0) + 1
        
        res = 0

        for i in reversed(sorted(cntList.values())):
            res += i * n
            n -= 1

        return res