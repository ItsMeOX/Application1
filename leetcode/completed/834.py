from typing import List
from collections import defaultdict

# This is a question of 'rerooting DP '.
#        0
#       / \
#      1   2
#         /|\
#        3 4 5
# For node = 0,
# the distance between 0th node and all other nodes will be 1 + 1 + 2 + 2 + 2 = 8.
# Now, if we want the answer for 2, if we move from node 0 to node 2,
# the distance from 2 -> 0, 2 -> 1 will increase by 1,
# and the distance from 0 -> 2, 0 -> 3, 0 -> 4, 0 -> 5 will decrease by 1.
# Hence, the res for node 2 will be 8 + 2 - 4 = 6,
# the formula will be res[i] = res[parent of i]  + ( n. of nodes excluding i + i_child ) - ( i + i_child )
#                     res[2] = res[0] + ( n - child[2] ) - child[2]
#                     res[2] = 8 + ( 6 - 4 ) - 4
#                     res[2] = 6

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        child = [1] * n
        res   = [0] * n
        adjList = defaultdict(list)

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        # count child + self number
        # also calculate the res for root
        def dfs(node, depth, prev):
            depth += 1
            for nei in adjList[node]:
                if nei != prev:
                    child[node] += dfs(nei, depth, node)
                    res[0] += depth

            return child[node]
        
        # calculate res for each node
        def dfs2(node, prev):
            if node:
                res[node] = res[prev] + ( n - child[node] ) - child[node]

            for nei in adjList[node]:
                if not res[nei]:
                    dfs2(nei, node)

        dfs(0, 0, 0)
        dfs2(0, 0)

        return res