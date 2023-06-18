class Solution:
    def minSideJumps(self, obstacles: list[int]) -> int:
        # no obstacle: 
        # dfs(i+1, same line)
        # obstacle: 
        # lines: [1,2,3]
        # if current_line != line
        #     dfs(i+1, line)
        dp = {}
        def dfs(i, line):
            if i == len(obstacles)-1:
                return 0
            if (i, line) in dp:
                return dp[(i, line)]
            res = 0
            if obstacles[i+1] != line:
                res = dfs(i+1, line)
            else:
                temp = []
                for l in [1,2,3]:
                    if l != line and obstacles[i] != l:
                        temp.append(1+dfs(i+1, l))
                res = min(temp)
            dp[(i, line)] = res
            return res

        return dfs(0, 2)
    
# class Solution:
#     def minSideJumps(self, obstacles: list[int]) -> int:
#         dp = [1,0,1]

#         for i in range(1, len(obstacles)):
#             for j in range(3):
#                 if obstacles[i] == j+1:
#                     dp[j] = float('inf')
#                 else:
#                     dp[j] = min(
#                         dp[0] + (0 if j==0 else 1) + (float('inf') if obstacles[i]==1 else 0),
#                         dp[1] + (0 if j==1 else 1) + (float('inf') if obstacles[i]==2 else 0),
#                         dp[2] + (0 if j==2 else 1) + (float('inf') if obstacles[i]==3 else 0)
#                     )

#         return min(dp)