from typing import List
from heapq import heappop, heappush
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)
        for u, v, price in flights:
            adjList[u].append((v, price))

        res = float('inf')
        q = [] # price, k, node
        for next_node, price in adjList[src]:
            heappush(q, (price, -k, next_node))

        visited = {}
        visited[src] = -k

        while q:
            cur_price, k, node = heappop(q)

            if node == dst:
                return cur_price

            if k == 0:
                continue  

            for next_node, next_price in adjList[node]:
                if next_node in visited and k > visited[next_node]: # if more steps, then skip
                    continue
                visited[node] = k
                heappush(q, (cur_price + next_price, k+1, next_node))

        return -1
