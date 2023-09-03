from typing import List
from collections import deque, defaultdict

# Here instead of using routes[i] as nodes, we use routes as node,
# as size of routers is only 1 <= N <= 500.
# If two routes have any same value, we will connect them together.
# At last, perform a BFS and find the shortest path between source and target.
# If not found, return -1.

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        n = len(routes)
        routes = list(map(set, routes))

        adjList = defaultdict(list)

        q = deque()
        visited = set()
        target_stop = set()

        for i in range(n):
            if source in routes[i]:
                q.append((1, i))
                visited.add(i)
            if target in routes[i]:
                target_stop.add(i)
            for j in range(i+1, n):
                if any(bus_stop in routes[j] for bus_stop in routes[i]):
                    adjList[i].append(j)
                    adjList[j].append(i)

        while q:
            bus_cnt, bus_stop = q.popleft()

            if bus_stop in target_stop:
                return bus_cnt

            for nei in adjList[bus_stop]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((bus_cnt + 1, nei))

        return -1
    