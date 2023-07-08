class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        if n <= 7:
            return n*(n+1) // 2
        else:
            weeks = 0
            while n > 6:
                weeks += 1
                n -= 7
            for i in range(1, n+1):
                res += i + weeks
            return res + ((weeks-1)*(weeks)//2)*7 + (7*8*weeks)//2