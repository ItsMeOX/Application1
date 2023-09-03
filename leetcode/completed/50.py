
# x^n = x^(2 * (n/2)) for n is even.
# x^n = x^(n-1+1)
#     = x^(n-1) * x
#     = x^(2 * (n-1)/2) * x for n is odd.
# Base case: if n == 0, x^0 = 1.
# If n < 0 : return 1 / myPow(x, -n) 

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n < 0 : return 1 / self.myPow(x, -n)

        if n % 2 == 0:
            return self.myPow(x*x, n / 2)
        else:
            return x * self.myPow(x*x, (n-1)/2)