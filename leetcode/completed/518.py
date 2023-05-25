# class Solution:
#     def change(self, amount: int, coins: list[int]) -> int: 
#         if not amount: return 1

#         memo = {}

#         def dfs(i, c):
#             if c > amount:
#                 return 0
            
#             if c == amount:
#                 return 1
            
#             if (i,c) in memo:
#                 return memo[(i,c)]

#             count = 0
#             for coin in coins:
#                 if coin >= i:
#                     count += dfs(coin, c+coin)

#             memo[(i,c)] = count

#             return count    

#         res = 0
#         for coin in coins:
#             res += dfs(coin, coin)


#         return res
    
class Solution:
    def change(self, amount: int, coins: list[int]) -> int: 
        memo = {}

        def dfs(i, c):
            if c > amount or i == len(coins):
                return 0
            
            if c == amount:
                return 1

            if (i,c) in memo:
                return memo[(i,c)]

            memo[(i,c)] = dfs(i, c + coins[i]) + dfs(i+1, c)

            return memo[(i,c)]    

        return dfs(0, 0)

sol = Solution()
print(sol.change(1000, [2,3,5]))