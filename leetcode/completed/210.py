from typing import List
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        indegree = [0] * numCourses

        for dst, src in prerequisites:
            adjList[src].append(dst)
            indegree[dst] += 1
        
        q = deque()
        for i in range(numCourses):
            if not indegree[i]:
                q.append(i)

        counter = 0
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            counter += 1

            for nei in adjList[node]:
                indegree[nei] -= 1
                
                if not indegree[nei]:
                    q.append(nei)
        
        return res if counter == numCourses else []