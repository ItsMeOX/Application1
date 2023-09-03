from typing import List
from collections import defaultdict
from heapq import heappush, heappop

# Firstly create a adjlist.
# Then perform a dijsktra algorithm and find the shortest path from n to every other node.
# For dijsktra, we keep a min heap and continue traversing from current shortest path, and we only traverse to next node if 
# the distance of next node is > current distance.
# We then traverse from node 1, and we only traverse to next node if the distance of (next node -> n th node) < distance of (current node -> n th node).
# If we ever reach n th node, then there is a valid restricted path, so add 1 to res.

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        distance = [float('inf')] * (n+1)
        distance[n] = 0
        adjList = defaultdict(list)
        MOD = 10 ** 9 + 7

        for u, v, w in edges:
            adjList[u].append((v, w))
            adjList[v].append((u, w))
        
        heap = []
        heap.append((0, n))

        while heap:
            cur_w, node = heappop(heap)
            if cur_w > distance[node]: continue
            for nei, w in adjList[node]:
                if cur_w + w < distance[nei]:
                    distance[nei] = cur_w + w
                    heappush(heap, (cur_w + w, nei))
            
        memo = {}
        def dfs(node):
            if node == n:
                return 1

            if node in memo:
                return memo[node]
            res = 0
            for nei, _ in adjList[node]:
                if distance[nei] < distance[node]:
                    res += dfs(nei) % MOD
            
            memo[node] = res

            return res

        return dfs(1) % MOD