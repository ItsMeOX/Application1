from heapq import heappop, heappush
from typing import List
from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adjList = defaultdict(list)
        for i, edge in enumerate(edges):
            node1, node2 = edge
            adjList[node1].append((node2, succProb[i]))
            adjList[node2].append((node1, succProb[i]))
        
        heap = [] # (cur_prob, prob, node)
        heappush(heap, (-1, -1, start))
        visited = set()
        
        while heap:
            cur_p, p, node = heappop(heap)
            if node not in visited:
                visited.add(node)
                if node == end:
                    return -cur_p
                for n, p in adjList[node]:
                    heappush(heap, (cur_p*p, -p, n))
                    
        return 0