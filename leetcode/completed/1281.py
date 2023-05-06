class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod, sum = 1 , 0
        while n > 0:
            sum += n%10
            prod *= n%10
            n//=10

        return prod - sum
        

sol = Solution()
print(sol.subtractProductAndSum(15))