from typing import List
from collections import defaultdict
from heapq import heappop, heappush

# nodes naming:
# a-b-c-d

# firstly we keep track of the three largest nodes for each edge,
# here we choose 3 because for example we have node b, we need at most 3 more different nodes.
# then we iterate through every edge. For every edge (u, v), u will be b, and v will be c.
# we then search for 3 of the largest valued neighbours of b and c, which are a at leftmost and b at rightmost.
# we have make sure that we do not rechoose nodes by making sure that a != c and d != a and d != b.
# at every four nodes chosen, we compare the sum of values of the four nodes with our res and return the max res.

class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        adjList = defaultdict(list)

        for u, v in edges:
            heappush(adjList[u], (scores[v], v))
            if len(adjList[u]) > 3:
                heappop(adjList[u])
            heappush(adjList[v], (scores[u], u))
            if len(adjList[v]) > 3:
                heappop(adjList[v])

        res = -1
        # a b c d
        for b, c in edges:
            for a_score, a in adjList[b]:
                if a == c: continue
                for d_score, d in adjList[c]:
                    if d == a or d == b: continue
                    res = max(res, a_score + d_score + scores[b] + scores[c])

        return res
    

# my initial (wrong) approach:
class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        res = 0

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        for key in adjList.keys():
            adjList[key].sort(key = lambda i: -scores[i])

        def dfs(i, k, score):
            score += scores[i]
            if k == 4:
                return score

            res = 0
            for nei in adjList[i]:
                if nei not in visited:
                    visited.add(nei)
                    res = dfs(nei, k+1, score)
                    visited.remove(nei)
                    # here breaking after greedily selecting the largest valued node will not work because of duplicated value nodes
                    # for example: 
                    # values = [1,1,3,2,1]
                    # edges  = [[4,1],[0,4],[0,1],[1,3],[2,0]]
                    # at i = 2, it will travel as following:
                    # 2 -> 0 -> 4 -> 1 
                    # 3 +  1 +  1 +  1 = 6
                    # while the correct answer is:
                    # 2 -> 0 -> 1 -> 3
                    # 3 +  1 +  1 +  2 = 7
                    if res: break

                    # ---------------------------------------
                    # if we chose to continue discovering next node if value of current node == value of next node:
                    # it will also not work as it will leads to TLE if the input is as following:
                    # values = [...]
                    # edges  = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5...]
                    # wrong code:
                    # for j in range(len(adjList[i])):
                    #     if adjList[i][j] not in visited:
                    #         visited.add(adjList[i][j])
                    #         res = dfs(adjList[i][j], k+1, score)
                    #         visited.remove(adjList[i][j])
                    #         if res and j < len(adjList[i])-1 and scores[adjList[i][j+1]] != scores[adjList[i][j]]: break


            return res

        visited = set()
        for i in range(len(scores)):
            visited.add(i)
            res = max(res, dfs(i, 1, 0))
            visited.remove(i)

        return res if res else -1