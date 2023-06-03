# class Solution:
#     def maximumDetonation(self, bombs: list[list[int]]) -> int:
#         visited = set()

#         def dfs(i):
#             temp = 0
#             for j in range(len(bombs)):
#                 if j not in visited and (bombs[i][0]-bombs[j][0])**2 + (bombs[i][1]-bombs[j][1])**2 <= bombs[i][2] ** 2:
#                     visited.add(j)
#                     temp += dfs(j) + 1

#             return temp


#         res = 0
#         for i in range(len(bombs)):
#             visited.clear()
#             visited.add(i)
#             res = max(res, dfs(i))

#         return res + 1

from collections import defaultdict
class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        adj = defaultdict(list)

        for i in range(len(bombs)):
            for j in range(i+1, len(bombs)):
                d = ((bombs[i][0]-bombs[j][0])**2+(bombs[i][1]-bombs[j][1])**2)**(0.5)
                if d <= bombs[i][2]:
                    adj[i].append(j)
                if d <= bombs[j][2]:
                    adj[j].append(i)
        
        res = 0
        def dfs(i, visited):
            if i in visited:
                return 0
            visited.add(i)
            for nei in adj[i]:
                dfs(nei, visited)
            return len(visited)
        
        for i in range(len(bombs)):
            res = max(res, dfs(i, set()))

        return res
        

        

sol = Solution()
print(sol.maximumDetonation([[1,1,100000],[100000,100000,1]]
))