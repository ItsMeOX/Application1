# Using fast exponential here.
# x^y = x^((y/2)*2) for y = even,
# x^y = x^(y-1+1)
#     = x^(y-1) * x
#     = x^(((y-1)/2)*2) * x

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n == 1: return 5
        MOD = 10 ** 9 + 7
        

        def pow(x, y):
            if y == 0: return 1
            temp = pow(x, y//2) % MOD
            if y & 1: return x * temp * temp
            else: return temp * temp

        return (pow(5, n//2+(n&1)) * pow(4, n//2)) % MOD
        # return (5 ** (n//2+n&1) * (4 ** n//2)) % MOD