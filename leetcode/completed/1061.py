from collections import defaultdict

# DFS solution (slow)

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        adjList = defaultdict(set)

        for i in range(len(s1)):
            adjList[s1[i]].add(s2[i])
            adjList[s2[i]].add(s1[i])

        def dfs(c):
            cur = c
            for nei in adjList[c]:
                if nei not in visited:
                    visited.add(nei)
                    cur = min(cur, dfs(nei))

            return cur

        res = ''
        for c in baseStr:
            visited = set()
            visited.add(c)
            res += dfs(c)
        
        return res

# Optimized adjList

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        adjList = defaultdict(set)

        for i in range(len(s1)):
            adjList[s1[i]].add(s2[i])
            adjList[s2[i]].add(s1[i])

        for key in adjList.keys():
            adjList[key].add(key)
            val = adjList[key]
            for key2, val2 in adjList.items():
                if key in val2:
                    adjList[key2] |= val
        
        res = ''
        for c in baseStr:
            if c in adjList:
                res += min(adjList[c])
            else:
                res += c

        return res
    
# DSU
# Iterate through s1[i] and s2[i] for i from 0 to length of str.
# Find the root of s1 and s2, if the root of s1 < s2, connect s2 to s1.
#                                               else, connect s1 to s2.
# Then iterate thourhg 'baseStr' and find the root of each character and append the root to 'res'.
# If the character is not in 'dsu' dictionary, then append the character.

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dsu = {}

        def find(x):
            while x in dsu and dsu[x] != x:
                x = dsu[x]
            return x
        
        def union(x, y):
            x, y = find(x), find(y)
            if x > y:
                dsu[x] = y
            else:
                dsu[y] = x

        for i in range(len(s1)):
            union(s1[i], s2[i])

        res = ''
        for c in baseStr:
            res += find(c)
        
        return res
