from collections import defaultdict
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        adj = defaultdict(list)

        # for i, m in enumerate(manager):
        #     if m != -1:
        #         adj[m].append(i)

        for i in range(n):
            adj[manager[i]].append(i)

        def dfs(i):
            if i not in adj:
                return 0

            res = 0
            for nei in adj[i]:
                res = max(res, informTime[i] + dfs(nei))

            return res

        return dfs(headID)


sol = Solution()
print(sol.numOfMinutes(n = 11, headID = 4, manager = [5,9,6,10,-1,8,9,1,9,3,4], informTime = [0,213,0,253,686,170,975,0,261,309,337]))