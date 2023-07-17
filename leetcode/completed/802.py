from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(i):
            if not graph[i] or i in res:
                res.add(i)
                return True

            if i in visited:
                return False

            visited.add(i)
            isSafe = True
            for nei in graph[i]:
                isSafe = isSafe & dfs(nei)

            if isSafe:
                res.add(i)

            return isSafe

        res = set()
        visited = set()

        for i in range(len(graph)):
            print(i, visited)
            visited = set()
            dfs(i)

        return list(res)
    

from collections import deque, defaultdict
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        indegree = [0] * len(graph)

        for i in range(len(graph)):
            for nei in graph[i]:
                adjList[nei].append(i)
                indegree[i] += 1
        
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for nei in adjList[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return sorted(res)


sol = Solution()
print(sol.eventualSafeNodes(graph = [[1,2],[2],[5],[0],[5],[],[]]))