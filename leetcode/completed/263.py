# Keep dividing n by 2, 3, 5 respectively until n not is divisible by any of 2, 3, 5.
# If the factors of n is only 2,3,5 , then the final n will be 1.
# Else, the factor of n will contain other number than than 2,3,5.

class Solution:
    def isUgly(self, n: int) -> bool:
        if not n:
            return False

        while not n % 2:
            n //= 2
        while not n % 3:
            n //= 3
        while not n % 5:
            n //= 5
        
        return n == 1