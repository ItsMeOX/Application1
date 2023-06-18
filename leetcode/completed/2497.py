# [17,49,-34,-17,-7,-23,24]
# [[3,1],[5,1],[0,3],[4,6],[1,4],[3,4],[6,3],[2,6],[5,2],[1,6],[6,0],[2,3],[3,5],[2,1],[0,2],[5,0],[0,4]]
# 6
# 90
from typing import List
from collections import defaultdict
class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        if not edges:
            return max(vals)

        adjList = defaultdict(list)
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        
        for key in adjList:
            adjList[key].sort(key = lambda e:-vals[e])
        
        def traverse(node):
            res = 0
            for nei in adjList[node][:k]:
                if vals[nei] > 0:
                    res += vals[nei]
            return res + vals[node]

        res = -float('inf')
        for key in adjList.keys():
            res = max(res, traverse(key))
        
        return max(res, max(vals))

    
sol = Solution()
print(sol.maxStarSum(vals = [-2,-1,-2], edges = [[0,2]], k = 1))

print(sol.maxStarSum([17,49,-34,-17,-7,-23,24],[[3,1],[5,1],[0,3],[4,6],[1,4],[3,4],[6,3],[2,6],[5,2],[1,6],[6,0],[2,3],[3,5],[2,1],[0,2],[5,0],[0,4]],6))