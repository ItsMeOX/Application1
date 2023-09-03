from typing import List

# Find all nodes with indegree = 0 as they cannot be accessed from any other nodes.

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        for _, v in edges:
            indegree[v] += 1
        
        res = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                res.append(i)

        return res