from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)

        for dst, src in prerequisites:
            if dst == src: return False
            adjList[src].append(dst)
        
        visited = [False] * numCourses
        inStack = [False] * numCourses

        def dfs(node):
            if inStack[node]:
                return True

            if visited[node]:
                return False

            inStack[node] = True
            visited[node] = True

            for nei in adjList[node]:
                if dfs(nei):
                    return True
                
            inStack[node] = False

            return False


        for i in range(numCourses):
            if dfs(i):
                return False


        return True
    

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool: # kahn's algorithm
        adjList = defaultdict(list)
        indegree = [0] * numCourses

        for dst, src in prerequisites:
            if dst == src: return False
            adjList[src].append(dst)
            indegree[dst] += 1
        
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        counter = 0

        while q:
            node = q.popleft()
            counter += 1

            for nei in adjList[node]:
                indegree[nei] -= 1

                if not indegree[nei]:
                    q.append(nei)


        return True if counter == numCourses else False