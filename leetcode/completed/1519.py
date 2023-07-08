from typing import List
from collections import defaultdict
import copy

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adjList = defaultdict(list)
        res = [1] * n
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)

        q = []
        q.append((0, {})) # node, dictionary
        visited = set()
        visited.add(0)

        while q:
            node, dictionary = q.pop()
            dictionary = copy.deepcopy(dictionary)
            if labels[node] in dictionary:
                for i in dictionary[labels[node]]:
                    res[i] += 1
            if labels[node] not in dictionary:
                dictionary[labels[node]] = []
            dictionary[labels[node]].append(node)
            for nei in adjList[node]:
                if nei not in visited:
                    q.append((nei, dictionary))
                    visited.add(nei)
        return res
    
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adjList = defaultdict(list)
        res = [1] * n
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)

        visited = set()

        def dfs(node):
            visited.add(node)
            cnt = [0] * 26
            cnt[ord(labels[node])-ord('a')] += 1
            for nei in adjList[node]:
                if nei not in visited:
                    child_cnt = dfs(nei)
                    for i in range(26):
                        cnt[i] += child_cnt[i]
            res[node] = cnt[ord(labels[node])-ord('a')]
            return cnt
        
        dfs(0)
        
        return res

sol = Solution()
print(sol.countSubTrees(4, [[0,1],[1,2],[0,3]], 'bbbb'))