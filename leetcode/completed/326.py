class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False

        temp = 1
        while temp <= n:
            if temp == n:
                return True
            temp *= 3

        return False
    
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False

        while n % 3 == 0:
            n //= 3

        return n == 1