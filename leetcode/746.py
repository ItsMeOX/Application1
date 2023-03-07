class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        for idx in range(len(cost)-3,-1,-1):
            cost[idx] += min(cost[idx+1], cost[idx+2])

        return min(cost[0],cost[1])
    

# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
    
#         for idx in range(2,len(cost)):

#             cost[idx] += min(cost[idx-1], cost[idx-2])


#         return min(cost[-2],cost[-1])