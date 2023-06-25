from typing import List

class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        res = [0]

        def dfs(i):
            if i >= len(cost):
                return 0

            left, right = dfs(2*i + 1), dfs(2*i+1 + 1)

            res[0] += abs(left - right)

            return cost[i] + max(left, right)
        
        dfs(0)

        return res[0]

    
sol = Solution()
print(sol.minIncrements())