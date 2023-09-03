from typing import List

# Here edges of complete components = N(N-1)/2 , N = number of nodes.
# So, we just have to find 
# 1. number of nodes in each components
# 2. number of edges in each components.
# Then for each component, check if N(N-1)/2 == number of edges holds,
# if true then res += 1.

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        root = [i for i in range(n)]
        size = [1] * n # number of nodes
        count = [0] * n # number of edges

        def find(a):
            while root[a] != a:
                a = root[a]
            return a
        
        def union(a, b):
            a_par = find(a)
            b_par = find(b)

            if a_par == b_par: return

            if size[a_par] > size[b_par]:
                size[a_par] += size[b_par]
                root[b_par] = a_par
            else:
                size[b_par] += size[a_par]
                root[a_par] = b_par
        
        for u, v in edges:
            union(u, v)
            count[find(v)] += 1
        
        seen = set()
        res = 0
        
        for i in range(n):
            par = find(i)
            if par in seen: continue
            seen.add(par)
            if count[par] == size[par]*(size[par]-1)//2:
                res += 1
        
        return res
    
from collections import defaultdict

# BFS solution.
# Start a BFS at every unvisited nodes.
# For every BFS, initalize 'node' and 'edge' which are no. of nodes and no. of edges in each components.
# After BFS, check if edge / 2 == node * (node-1) / 2, (edge/2 as we have traversed an edge twice (from u to v and v to u))
#                     edge == node * (node-1).

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        q = []
        visited = set()
        adjList = defaultdict(list)
        res = 0

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        for i in range(n):
            if i not in visited:
                node = 0
                edge = 0
                q.append(i)
                visited.add(i)
                while q:
                    cur_node = q.pop()
                    node += 1
                    for nei in adjList[cur_node]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
                        edge += 1
                if edge == node * (node-1):
                    res += 1
    
        return res