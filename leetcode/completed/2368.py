from typing import List
from collections import defaultdict, deque

# Add restricted nodes to visited set, then perform a dfs at node 0,
# every time we explored a unvisited node we add 1 to res.

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = set(restricted)
        res = 0
        q = deque([0])

        while q:
            node = q.popleft()
            if node in visited:
                continue
            visited.add(node)
            res += 1

            for nei in adjList[node]:
                q.append(nei)
        
        return res