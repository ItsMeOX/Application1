from typing import List
from collections import defaultdict

# The number of MHT will be either one or two. (if there is 3, the middle one will be the MHT)
# Starting from leaf nodes, 
# keep cutting the leaf nodes simultaneously, until node left < 2,
# the remaining nodes will be the centroid of the tree,
# hence the MHT.

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]

        adjList = defaultdict(set)
        for u, v in edges:
            adjList[u].add(v)
            adjList[v].add(u)
        
        leaves = []

        for node in range(len(adjList)):
            if len(adjList[node]) == 1:
                leaves.append(node)
        
        node_left = n

        while node_left > 2:
            node_left -= len(leaves)
            new_leaves = []
            while leaves:
                leaf = leaves.pop()
                nei = adjList[leaf].pop()
                adjList[nei].remove(leaf)
                if len(adjList[nei]) == 1:
                    new_leaves.append(nei)
            leaves = new_leaves
        
        return leaves