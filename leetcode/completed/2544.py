class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sign = 1 if len(str(n)) & 1 else -1
        res = 0
        while n:
            res += n % 10 * sign
            n //= 10
            sign = -sign
        
        return res