class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return (-1 if dp[-1] == amount+1 else dp[-1])


                

    
sol = Solution()
print(sol.coinChange([2147483647], 2))