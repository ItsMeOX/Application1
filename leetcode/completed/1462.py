from typing import List
from collections import deque, defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = defaultdict(list)
        res = []

        for dst, src in prerequisites:
            adjList[src].append(dst)

        for dest, src in queries:
            q = deque()
            q.append(src)
            visited = set()
            isRes = False
            while q:
                node = q.popleft()
                if dest == node:
                    res.append(True)
                    isRes = True
                    break
                for nei in adjList[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            if not isRes:
                res.append(False)

        return res

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]: # kahn's algorithm
        adjList = defaultdict(list)
        ancestors = defaultdict(set)
        indegree = [0] * numCourses
        q = deque()
        res = []

        for dst, src in prerequisites:
            adjList[src].append(dst)
            indegree[dst] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()

            for nei in adjList[node]:
                indegree[nei] -= 1
                ancestors[nei].add(node)
                ancestors[nei].update(ancestors[node])

                if indegree[nei] == 0:
                    q.append(nei)

        for dest, src in queries:
            if src in ancestors[dest]:
                res.append(True)
            else:
                res.append(False)

        return res
