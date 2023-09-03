from typing import List
from collections import deque

# Perform a bfs here, no need to use dijsktra's algorithm, as we can move one by one step using bfs and the first which moves across all the
# nodes will be the shortest path.
# Firstly, append all nodes to queue.
# For item in queue, we have (current path length, current node, mask that masks which node we have visited).
# We also initialized a 'visited' set which stores (current path length, current mask), as there is no point walking back without having visited 
# a node.
# Each queue pop, we will masks 'mask' with the current node number, 
# for example:
# number of nodes = 5, 
# initial we have mask of 00000,
# if we have visited a node, we will mask 'mask' to 10000.
# If our 'mask' is 11111, that means we have visited all nodes, so return current path length, and that will be our answer.

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if not graph[0]:
            return 0

        n = len(graph)
        q = deque() # (cur_len, node, mask)
        visited = set()

        for i in range(n):  
            q.append((0, i, 0))

        while q:
            cur_len, node, mask = q.popleft()
            mask |= (1 << node)

            if mask == (1 << n) - 1:
                return cur_len

            for nei in graph[node]:
                if (nei, mask) not in visited:
                    visited.add((nei, mask))
                    q.append((cur_len+1, nei, mask))