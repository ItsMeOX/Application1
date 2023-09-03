from typing import List
from collections import deque, defaultdict

# Using topological sort here, because that we need to detect circle.
# Create adj list and indegree list,
# append all the indegree 0 nodes to q.
# Here we will initialize a list of length 26 for each node, and add 1 to the index of alphabet every time we visit a node.
# Then we will update the list of neighbour node by comparing from a ~ z, and update each element with the larger one.
# Each traverse, we will update 'res' with maximum element in list.
# We will also only traverse to next node if the indegree of that node is 0, this allows us to not traverse nodes that are in cycle,
# also add 1 to 'seen' every time we visit a node.
# At last, if 'seen' is equal to no. of node, then return 'res', else return -1 indicating that there is cycle.

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        indegree = [0] * len(colors)
        adjList = defaultdict(list)
        memo = [[0]*26 for _ in range(len(colors))]
        res = -1
        seen = 0

        for u, v in edges:
            adjList[u].append(v)
            indegree[v] += 1

        q = []

        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.pop()
            memo[node][ord(colors[node])-ord('a')] += 1
            res = max(res, max(memo[node]))
            seen += 1
            for nei in adjList[node]:
                indegree[nei] -= 1
                for i in range(26):
                                
                    memo[nei][i] = max(memo[nei][i], memo[node][i])
                if indegree[nei] == 0:
                    q.append(nei)
        
        return res if seen == len(colors) else -1

# DFS (not effecient)

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        if not edges: return 1
        indegree = [0] * len(colors)
        outdegree = [0] * len(colors)
        adjList = defaultdict(list)
        memo = [[0]*26 for _ in range(len(colors))]
        res = -1

        for u, v in edges:
            adjList[u].append(v)
            indegree[v] += 1
            outdegree[u] += 1

        def dfs(node):
            nonlocal res
            
            memo[node][ord(colors[node])-ord('a')] += 1

            if outdegree[node] == 0: # if it is leaf node, then compare with res.
                res = max(res, max(memo[node]))

            for nei in adjList[node]:
                for i in range(26):
                    memo[nei][i] = max(memo[nei][i], memo[node][i])
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    dfs(nei)
            
        t = []
        for i in range(len(indegree)): # have to append node to a temporary list first or else indegree will be changed.
            if indegree[i] == 0 and outdegree[i]:
                t.append(i)

        for node in t:
            dfs(node)
        
        return res