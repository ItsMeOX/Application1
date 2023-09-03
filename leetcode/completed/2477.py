from typing import List
from collections import defaultdict
from math import ceil

# We will first traverse from nodes which indegree is 1, which means it is only outgoing,
# then we will traverse until we meet a node which indegree > 2, as we want to first accumulate the total people passing there so we know that
# what is the least car needed to fetch them all.
# If we reach node 0, we will also stop traversing.
# Every time we move to neigbour node, we will add people count of current node to that neighbour node, and 
# we will decrease the indegree of neighbour node and current node by 1, this trick is similar to Khan's algorithm.
# Every time we move to neighbour node, we will also add fuel needed to 'res' by ceil(people count / seats).
# Note that we want to add fuel needed to 'res' only one time in 'for neighbor loop', so we will add another 'first_seen' array, 
# and we will only add fuel needed if first_seen[nei] == 1.

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        adjList = defaultdict(list)
        indegree = [0] * n
        count = [1] * n
        first_seen = [1] * n

        for u, v in roads:
            adjList[u].append(v)
            adjList[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        res = 0
        q = [] # (node)

        for i in range(len(indegree)):
            if indegree[i] == 1:
                q.append(i)

        while q:
            node = q.pop()
            if node == 0: continue
            first_seen[node] = 0

            for nei in adjList[node]:
                count[nei] += count[node]
                indegree[node] -= 1
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    q.append(nei)
                if first_seen[nei]:
                    res += ceil(count[node] / seats)

        return res
    
# DFS solution:
# Starting from node 0, traverse to neighbour and get the total count of people from its descendants,
# then res += (total people count / seats) for every nodes except node 0.

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        adjList = defaultdict(list)
        for u, v in roads:
            adjList[u].append(v)
            adjList[v].append(u)

        res = 0

        def dfs(node, prev):
            nonlocal res
            count = 1

            for nei in adjList[node]:
                if nei == prev: continue
                count += dfs(nei, node)
            
            if node != 0:
                res += ceil(count / seats)
        
            return count

        dfs(0, 0)
        return res