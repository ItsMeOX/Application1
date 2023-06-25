class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        def dp(i, remain, isStart):
            if remain == 0:
                return 1
            if i == n:
                # print(f"remain: {remain}")
                return 0
 
            res = dp(i+1, k, isStart)
 
            if isStart:
                res += dp(i+1, remain, False)
            else:
                res += dp(i, remain-1, True)

            return res % MOD
        
        return dp(0, k, True)
    


sol = Solution()
print(sol.numberOfSets(3, 1))