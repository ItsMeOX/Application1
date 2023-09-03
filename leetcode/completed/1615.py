from typing import List
from collections import defaultdict

# Check every pair of nodes,
# add up indegree of two nodes, if two nodes are connected, -1.
# Ans will be the maximum sum of indegree between every pair.

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adjList = defaultdict(set)
        for u, v in roads:
            adjList[u].add(v)
            adjList[v].add(u)

        res = 0
        for i in range(n):
            for j in range(i):
                res = max(res, len(adjList[i])+len(adjList[j])-(i in adjList[j]))

        return res