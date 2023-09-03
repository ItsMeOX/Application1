from typing import List

# Find the MST among all the points.
# Cost of edges will be the manhattan distance between two nodes.

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = [] # (i, j, cost)

        for i in range(len(points)):
            for j in range(len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                edges.append((i, j, abs(x1-x2)+abs(y1-y2)))
        
        edges.sort(key = lambda e: e[2])

        par = [i for i in range(len(points))]

        def find(a):
            while a != par[a]:
                a = par[a]
            return a
        
        def union(a, b):
            ar, br = find(a), find(b)
            if ar == br: return False
            par[br] = par[ar]
            return True

        edge = 0
        i = 0
        res = 0
        while edge < len(points)-1:
            p1, p2, cost = edges[i]
            if union(p1, p2):
                res += cost
                edge += 1
            i += 1

        return res



from heapq import heappop, heappush
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distance = lambda p1, p2: abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

        res = 0
        edge = 0
        heap = [] # (cost, node)
        heap.append((0, 0))
        visited = set()

        while edge < len(points):
            cost, i = heappop(heap)
            if i in visited: continue
            visited.add(i)
            edge += 1
            res += cost

            for j in range(len(points)):
                if j not in visited:
                    heappush(heap, (distance(points[i], points[j]), j))

        return res