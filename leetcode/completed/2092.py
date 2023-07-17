from typing import List
from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        adjList = defaultdict(list)

        for src, dst, time in meetings:
            adjList[src].append((dst, time))
            adjList[dst].append((src, time))

        q = []
        q.append((0, 0))
        q.append((0, firstPerson))

        res = set()

        while q:
            cur_time, node = heappop(q)
            if node in res:
                continue
            res.add(node)
            for nei, time in adjList[node]:
                if time >= cur_time:
                    heappush(q, (time, nei))

        return res
    
    
sol = Solution()
print(sol.findAllPeople(4, [[3,1,3],[1,2,2],[0,3,3]], 3))