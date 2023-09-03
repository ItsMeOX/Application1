class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n > 1:
            temp = n % 2
            res += n // 2
            n //= 2
            n += temp

        return res
    
class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1