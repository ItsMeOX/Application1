from typing import List
from functools import cache
from bisect import bisect_right

# Sort offers by start and for each index,
# we either choose to take the trade or skip the trade.
# If we take the trade, then we have to start our next trade at trade which its start > current end,
# and we have to append current gold to our res.
# If we not take the trade, just i += 1.

class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort()
        starts = [offer[0] for offer in offers]

        @cache
        def dfs(i):
            if i == len(offers):
                return 0
            
            # not take
            res = dfs(i+1)

            # take
            index = bisect_right(starts, offers[i][1])
            res = max(res, dfs(index) + offers[i][2])

            return res

        return dfs(0)
    
    
class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort()
        starts = [offer[0] for offer in offers]
        dp = [0] * (len(offers)+1)
        for i in range(len(offers)-1, -1, -1):
            index = bisect_right(starts, offers[i][1])
            dp[i] = max(dp[i+1], dp[index] + offers[i][2])
            
        return dp[0]