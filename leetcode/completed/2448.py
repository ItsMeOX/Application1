from typing import List
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        lo, hi = 1, max(nums)
        res = float('inf')

        def getCost(num):
            cost_needed = 0
            for i in range(len(nums)):
                cost_needed += abs(nums[i]-num) * cost[i]
            return cost_needed

        while lo <= hi:
            # find val of mid
            m = (lo+hi) // 2
            # print(lo,m,hi)
            # if left quart < mid, move hi = m - 1
            left_quart = (lo+m) // 2       
            left_quart_cost = getCost(left_quart)
            
            # else move lo = m + 1
            right_quart = (hi+m) // 2 + 1
            right_quart_cost = getCost(right_quart)

            if left_quart_cost > right_quart_cost:
                lo = m + 1
            else:
                hi = m - 1
                
            res = min(getCost(m), left_quart_cost, right_quart_cost)

        
        return res

from typing import List
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        lo, hi = 1, max(nums)

        def getCost(num):
            cost_needed = 0
            for i in range(len(nums)):
                cost_needed += abs(nums[i]-num) * cost[i]
            return cost_needed

        while lo < hi:
            m = (lo+hi) // 2

            if getCost(m) < getCost(m+1):
                hi = m
            else:
                lo = m + 1
            
        return getCost(lo)

nums = [576257,268115,512826,523563,927189,39253,720661,35147,552624,847824,354489,760949,734966,571013]
cost = [842872,273313,503060,139143,367612,217125,271272,407727,199063,120280,819193,935689,624116,453146]

sol = Solution()
print(sol.minCost(nums, cost))

# 1  -> 691 l
# 2  -> 602
# 3  -> 521
# 4  -> 452 lq
# 5  -> 407
# 6  -> 382 
# 7  -> 361 m
# 8  -> 346    l  l,m
# 9  -> 349    lq h
# 10 -> 378 rq m
# 11 -> 417    rq
# 12 -> 478
# 13 -> 569 h  h