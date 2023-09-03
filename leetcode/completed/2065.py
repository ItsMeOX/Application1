from typing import List
from collections import defaultdict

# Initialize a adjacent list which key is a node and its value is a list of (neighbour, time needed to travel)
# Initialize 'res' to value to node 0.
#
# Perform a dfs which parameters are (current node, total time used, current quality) at node 0, 
# Base cases: if total time used > max time, return.
# Every time reach node 0, we check if current quality > res, if true then update res to current quality.
# Starting from node 0, we traverse to neighbour node and we keep track nodes we have visited, 
# if we have not visited current node, add the value of current node to 'quality'.
# Then we add current to 'visited', so that next time we reach this we will not add current node value to 'quality'.
# We will only remove current node from 'visited' after we done exploring all routes after current node, 
# so here we initiliaze a boolean 'flag' and set it to true if we first meet this node, and 
# we will only remove this node from 'visited' and subtract current node val from 'quality' if flag is true. 

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        adjList = defaultdict(list) # src: [...(dst, time)]
        visited = set()
        res = values[0]

        for src, dst, time in edges:
            adjList[src].append((dst, time))
            adjList[dst].append((src, time))

        def dfs(node, total_time, quality):
            nonlocal res
            if total_time > maxTime:
                return
            if node == 0:
                res = max(res, quality)

            flag = False # flag = first meet
            if node not in visited:
                flag = True
                visited.add(node)
                quality += values[node]

            for nei, time in adjList[node]:
                dfs(nei, total_time+time, quality)
            
            if flag:
                quality -= values[node]
                visited.remove(node)

        dfs(0, 0, 0)

        return res