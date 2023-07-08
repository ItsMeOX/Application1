from collections import defaultdict
from typing import List

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjList = defaultdict(list) 

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        res = 0
        def dfs(node, prev):
            nonlocal res
            cur_hasApple = False
            childHasApple = set()

            if node in adjList:
                for nei in adjList[node]:
                    if nei != prev:
                        childHasApple.add(dfs(nei, node))

            cur_hasApple = hasApple[node] or any(childHasApple) # check if current node is on path

            if cur_hasApple:
                res += 1    

            return cur_hasApple

        dfs(0, 0)

        return (res-1) * 2 if res else 0
    

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjList = defaultdict(list) 

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        def dfs(node, prev):
            time = 0
            for nei in adjList[node]:
                if nei != prev:
                    child_time = dfs(nei, node)
                    if child_time or hasApple[nei]:
                        time += (child_time + 2)
        
            return time

        return dfs(0, 0)
