class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        for i in range(15, -1, -1):
            x = 3 ** i
            if n >= x:
                n -= x
            if n == 0:
                return True
        return False
    


sol = Solution()
print(sol.checkPowersOfThree(21))