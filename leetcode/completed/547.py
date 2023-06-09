class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int: #dfs O(n^2), O(n)
        l = len(isConnected)
        visited = set()
        res = 0

        def dfs(i):
            for j in range(l):    
                if i != j and isConnected[i][j] and j not in visited:
                    visited.add(j)
                    dfs(j)

        for i in range(l):
            if i not in visited:
                visited.add(i)
                dfs(i)
                res += 1

        return res
    
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int: # union find 
        l = len(isConnected)
        parents = [n for n in range(l)]
        rank = [1] * l
        res = set()

        print(parents)

        def union(a, b):
            a_root = find(a)
            b_root = find(b)

            if a_root == b_root:
                return
            
            if rank[a_root] > rank[b_root]:
                parents[b_root] = parents[a_root]
                rank[a_root] += rank[b_root]
            else:
                parents[a_root] = parents[b_root]
                rank[b_root] += rank[a_root]


        def find(a):
            while parents[a] != a:
                a = parents[a]
            return a
        
        for i in range(l):
            for j in range(l):
                if isConnected[i][j]:
                    union(i, j)

        for p in parents:
            res.add(find(p))

        return len(res)

sol = Solution()
print(sol.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
))