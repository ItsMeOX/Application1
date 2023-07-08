from collections import defaultdict, deque
from typing import List

class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        res = float('inf')
        q = deque()
        for node in adjList.keys():
            q.append(node)
            distance = 1
            distances = [-1] * n
            parents = [-1] * n
            start = node
            parents[start] = start
            distances[start] = 0

            while q:                
                for _ in range(len(q)):
                    node = q.popleft()
                    for nei in adjList[node]:
                        if distances[nei] == -1:
                            parents[nei] = node
                            distances[nei] = distance
                            q.append(nei)
                        elif parents[node] != nei:
                            res = min(res, distances[nei] + distances[node] + 1)
                distance += 1
    
        return res    
    
sol = Solution()
print(sol.findShortestCycle(n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]))