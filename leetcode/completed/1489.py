from typing import List

# MST -> Kruskal's algorithm.
# Sort the edges by cost in increasing order,
# if edge[i][0] and edge[i][1] does not form cycle in current built graph,
# then append it to our graph.

# Critical edge: if we remove this edge, then either edge < n-1 or cost > min_cost.
# Non critical edge: if we force this edge, the cost == min_cost. (no need to check if edge < n-1 because it is guaranteed to be a valid spanning tree)

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indices = {(edges[i][0], edges[i][1]): i for i in range(len(edges))}
        edges.sort(key = lambda e: e[2])

        def find(a, par):
            while par[a] != a:
                a = par[a]
            
            return a
        
        def union(a, b, par, rank):
            ar, br = find(a, par), find(b, par)
            if ar == br: return False
            if rank[ar] > rank[br]:
                par[br] = par[ar]
                rank[ar] += rank[br]
            else:
                par[ar] = par[br]
                rank[br] += rank[ar]
            return True

        # get min cost
        min_par = [i for i in range(n)]
        min_rank = [1] * n
        min_cost = 0
        for u, v, cost in edges:
            if union(u, v, min_par, min_rank):
                min_cost += cost
        print(min_cost)

        critical = []
        pseudo_critical = []
        for i in range(len(edges)):
            # ignore this
            u, v, cost = edges[i]
            ignore_rank = [1] * n
            ignore_par = [k for k in range(n)]
            ignore_cost = 0
            ignore_edges = 0
            for j in range(len(edges)):
                if i == j: continue
                u2, v2, cost2 = edges[j]
                if union(u2, v2, ignore_par, ignore_rank):
                    ignore_edges += 1
                    ignore_cost += cost2
            
            if ignore_edges < n-1 or ignore_cost > min_cost:
                critical.append(indices[(u, v)])
                continue

            force_rank = [1] * n
            force_par = [k for k in range(n)]
            force_cost = cost
            union(u, v, force_par, force_rank)
            for j in range(len(edges)):
                u2, v2, cost2 = edges[j]
                if union(u2, v2, force_par, force_rank):
                    force_cost += cost2

            if force_cost == min_cost:
                pseudo_critical.append(indices[(u, v)])
        
        return [critical, pseudo_critical]
    
sol = Solution()
print(sol.findCriticalAndPseudoCriticalEdges(n = 6, edges = [[0,1,1],[1,2,1],[0,2,1],[2,3,4],[3,4,2],[3,5,2],[4,5,2]]))