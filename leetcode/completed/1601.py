from typing import List
from collections import defaultdict

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        res = 0
        def backtrack(i, indegree, count):
            nonlocal res
            if i == len(requests):
                for i in indegree:
                    if i != 0:
                        return
                res = max(res, count)
                return


            indegree[requests[i][0]] -= 1
            indegree[requests[i][1]] += 1
            backtrack(i+1, indegree, count+1)

            indegree[requests[i][0]] += 1
            indegree[requests[i][1]] -= 1
            backtrack(i+1, indegree, count)

            # remember to subtract back if skipping first
            # backtrack(i+1, indegree, count)
            # indegree[requests[i][0]] -= 1
            # indegree[requests[i][1]] += 1
            # backtrack(i+1, indegree, count+1)
            # indegree[requests[i][0]] += 1
            # indegree[requests[i][1]] -= 1


        indegree = [0] * n
        backtrack(0, indegree, 0)
        return res

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int: # wrong answer, but maybe doable?
        adjList = defaultdict(list)
        res = 0
        for f, t in requests:
            if f == t:
                res += 1
            else:
                adjList[f].append(t)
        
        def dfs(node, start, isFirst, visited):
            nonlocal res
            if not isFirst and node == start:
                return True
            
            isCyclic = False
            for nei in adjList[node]:
                if nei not in visited:
                    visited.add(nei)
                    isCyclic = dfs(nei, start, False, visited)
                    if isCyclic:
                        adjList[node].remove(nei)
                        res += 1
                        break
            
            return isCyclic
        
        for f, t in requests:
            dfs(f, f, True, set())

        return res
    
sol = Solution()
print(sol.maximumRequests(n = 2, requests = [[0,1],[1,0]]
))