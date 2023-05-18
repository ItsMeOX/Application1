class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1)
        dp[0] = 1
        mod = 10 ** 9 + 7
        res = 0

        for i in range(1, high + 1):
            if i - zero >= 0:
                dp[i] += dp[i - zero] % mod
            if i - one >= 0:
                dp[i] += dp[i - one] % mod

            if low <= i <= high:
                res += dp[i] % mod

        return res % mod
            

        # dp = [None] * (high + 1)

        # def dfs(count):
        #     if count > high:
        #         return 0
            
        #     if dp[count] != None:
        #         return dp[count]

        #     if count < low:
        #         res = dfs(zero + count) + dfs(one + count)
        #         dp[count] = res
        #         return res

        #     res = dfs(zero + count) + dfs(one + count) + 1
        #     dp[count] = res
        #     return res


            
        # return (dfs(low) + dfs(one)) % 1000000007

sol = Solution()
print(sol.countGoodStrings(1, 100000, 1, 1))