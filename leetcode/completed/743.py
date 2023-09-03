from heapq import heappop, heappush
from typing import List
from collections import defaultdict

# Perform Dijkstra's algorithm and update res with max cost from node k to every other node.
# If the amount of visited nodes < n, return -1.


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adjList = defaultdict(list)
        for u, v, cost in times:
            adjList[u].append((v, cost))

        distance = [float('inf')] * (n+1) # can also use dictionary instead of array of inf here.
        distance[k] = distance[0] = 0
        heap = [(0, k)] # (cost, node)

        res = 0

        while heap:
            cur_cost, node = heappop(heap)
            if distance[node] != cur_cost:
                continue

            res = max(res, cur_cost)

            for nei, cost in adjList[node]:
                if cur_cost + cost < distance[nei]:
                    distance[nei] = cur_cost + cost
                    heappush(heap, (cur_cost + cost, nei))


        for d in distance:
            if d == float('inf'): return -1
        
        return res