from typing import List
from bisect import bisect_left

# days = [1,4,6,7,8,20], costs = [2,7,15] for example,
# then we have three cases:
# 1. travel to next day. total_cost + costs[0]
# 2. travel to seven days after, if that day is not in 'days', keep skipping to next day. total_cost + costs[1].
# 3. for 30 days, it is same as (2). total_cost + costs[2]
# Instead of skipping to next day, we can use bisect left to search for i where days[i] >= next day.

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i >= len(days):
                return 0
            
            if i in memo:
                return memo[i]

            one = dfs(bisect_left(days, days[i] + 1)) + costs[0]
            seven = dfs(bisect_left(days, days[i] + 7)) + costs[1]
            eleven = dfs(bisect_left(days, days[i] + 30)) + costs[2]

            res = min(one, seven, eleven)
            memo[i] = res

            return res
        
        return dfs(0)
    
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        max_day = days[-1]
        dp = [0] * (max_day + 1)
        days = set(days)

        for i in range(1, max_day+1):
            if i in days:
                dp[i] = min(
                    dp[max(0, i-1)]+costs[0], 
                    dp[max(0, i-7)]+costs[1], 
                    dp[max(0, i-30)]+costs[2]
                )
            else:
                dp[i] = dp[i-1]
        
        return dp[-1]