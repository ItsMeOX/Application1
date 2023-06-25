from typing import List

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = {}
        MOD = 10 ** 9 + 7

        def dfs(i, fuel_left):
            if (i, fuel_left) in dp:
                return dp[(i, fuel_left)]

            res = 0
            if fuel_left < 0:
                return 0

            if i == finish:
                res += 1

            for j in range(len(locations)):
                if i != j:
                    res += dfs(j, fuel_left - abs(locations[i]-locations[j]))

            dp[(i, fuel_left)] = res
            return res

        return dfs(start, fuel) % MOD

sol = Solution()
print(sol.countRoutes(locations = [5,2,1], start = 0, finish = 2, fuel = 3))