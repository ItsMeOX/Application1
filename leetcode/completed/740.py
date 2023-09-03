
# Consider example arr: [3,2,3,2,3,4]
# We can rearrange it to [2,2,3,3,3,4]
# and if we pick 2, then we will take all 2, so we can convert the data in array to total sum of each num.
# Arr becomes [0, 0, 4, 9, 4] where i in the number and arr[i] is the total sum of i.
# This problem then becomes house robber problem, where we take or not take current arr[i].

class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        memo = {}
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        cu = [0] * (max(frequency.keys())+1)
        for key in frequency.keys():
            cu[key] = frequency[key] * key

        def dfs(i):
            if i >= len(cu):
                return 0
            
            if i in memo:
                return memo[i]
            
            not_take = dfs(i+1)
            take = dfs(i+2) + cu[i]

            res = max(not_take, take)
            memo[i] = res
            return res

        return dfs(0)
    
class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        cu = [0] * (max(frequency.keys())+1)
        for key in frequency.keys():
            cu[key] = frequency[key] * key

        for i in range(2, len(cu)):
            cu[i] = max(cu[i-1], cu[i-2] + cu[i])
        
        return cu[-1]