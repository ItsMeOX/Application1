from typing import List
from collections import defaultdict

# Suppose we have source: [1,2,3,4], target: [3,2,1,1], allowedSwaps: [[0,2], [0,3]]
# my approach is to perform a DFS for every i from 0 to len(source)-1,
# and build a counter dictionary for 'source' and 'target' for every components.
# For example, because we can traverse from 0 to 2 and 3, {0, 2, 3} will be a component.
# Here after buliding the counter dictionary, it will look like:
# counter1: {0: {1:1, 2:1, 3:1}, 1: {2: 1}}
# counter2: {0: {1:2, 3:1}, 1: {2: 1}}
# Then we iterate through key of counter1, 
# and subtract 'res' by if each key can be paired with counter2.
# 0: 1: can be only paired once with counter2, so res -= 1
#    2: cannot be paired, so res -= 0
#    3: can be paired once, so res -= 1
# 1: 2: can be paired once, so res -= 1.
# The final 'res' will be the element that cannot be swapped.

# DFS solution

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        res = len(source)

        # initialize adjlist
        adjList = defaultdict(list)
        for u, v in allowedSwaps:
            adjList[u].append(v)
            adjList[v].append(u)
        
        # get components
        visited = set()
        counter1 = defaultdict(dict)
        counter2 = defaultdict(dict)
        cur_idx = 0
        for i in range(len(source)):
            if i not in visited:
                visited.add(i)
                q = [i]
                while q:
                    node = q.pop()
                    counter1[cur_idx][source[node]] = counter1[cur_idx].get(source[node], 0) + 1
                    counter2[cur_idx][target[node]] = counter2[cur_idx].get(target[node], 0) + 1
                    for nei in adjList[node]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            cur_idx += 1
        
        # subtract same
        for key in counter1:
            for val in counter1[key]:
                val1 = counter1[key][val] if val in counter1[key] else 0
                val2 = counter2[key][val] if val in counter2[key] else 0
                res -= min(val1, val2)
        
        return res
        
# Union Find solution
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        self.par = [i for i in range(len(source))]
        self.rank = [1] * len(source)

        def find(a):
            while self.par[a] != a:
                a = self.par[a]
            return a
        
        def union(a, b):
            ar, br = find(a), find(b)
            if ar == br: return
            if self.rank[ar] > self.rank[br]:
                self.rank[ar] += self.rank[br]
                self.par[br] = ar
            else:
                self.rank[br] += self.rank[ar]
                self.par[ar] = br
        
        for u, v in allowedSwaps:
            union(u, v)
        
        counter = defaultdict(dict)
        for i in range(len(source)):
            par = find(i)
            num = source[i]
            counter[par][num] = counter[par].get(num, 0) + 1
        
        res = 0
        for i in range(len(target)):
            par = find(i)
            num = target[i]
            if num in counter[par]:
                counter[par][num] -= 1
                if not counter[par][num]:
                    del counter[par][num]
            else:
                res += 1

        return res