from typing import List
from collections import defaultdict

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        adjList = defaultdict(list)
        n = len(strs)
        str_len = len(strs[0])

        for i in range(n):
            for j in range(i+1, n):
                count = 0
                for k in range(str_len):
                    if strs[i][k] != strs[j][k]:
                        count += 1
                if count in (0, 2):
                    adjList[i].append(j)
                    adjList[j].append(i)
    
        visited = set()
        res = 0
        def dfs(i):
            for nei in adjList[i]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        for i in range(len(strs)):
            if i not in visited:
                res += 1
                dfs(i)
                visited.add(i)

        return res