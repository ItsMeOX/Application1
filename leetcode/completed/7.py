class Solution:
    def reverse(self, x: int) -> int:
        
        rev=0
        neg = False
        if x < 0:
            x =- x
            neg = True
        while x:
            mod = x % 10
            x //= 10
            rev = rev * 10 + mod

        if neg:
            rev = -rev

        if rev < -2147483648 or rev > 2147483647:
            return 0
            
        return rev