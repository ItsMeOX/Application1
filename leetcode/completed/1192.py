from typing import List
from collections import defaultdict

# Critical connections exists if and only if the connection is not part of a cycle in the graph.
# To detect cycle in graph, we define an array 'rank' and all rank of nodes to -1 initally.
# Then we perform a dfs, on every node, we set the rank of node to current depth.
# For example: 0 -> 1 -> 2 -> 3
# then rank[0] = 1
#      rank[1] = 2
#      rank[1] = 3
#      rank[1] = 4
# If we reach a node where rank is not -1 and rank is <= current depth,
# then we know that we have found a cycle.
# To remove all edges in the cycle,
# we return rank[node] as 'return_depth' when rank[node] <= depth.
# If the returned depth is <= current depth, then we know this edge is in a cycle, so remove it. (from the set)
# Lastly, the remaining edges that are not removed will be our answer.

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        rank = [-1] * n
        adjList = defaultdict(list)

        for u, v in connections:
            adjList[u].append(v)
            adjList[v].append(u)

        res = set(tuple(sorted([u, v])) for u, v in connections)

        def dfs(node, depth):
            if 1 <= rank[node] <= depth:
                return rank[node]
            rank[node] = depth
            min_return_depth = depth
            for nei in adjList[node]:
                if rank[nei] == depth - 1 or rank[nei] > depth:
                    continue
                return_depth = dfs(nei, depth + 1)
                min_return_depth = min(min_return_depth, return_depth)
                if return_depth <= depth:
                    res.remove(tuple(sorted([node, nei])))
            return min_return_depth

        dfs(0, 1)

        return res