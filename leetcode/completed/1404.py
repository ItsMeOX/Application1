class Solution:
    def numSteps(self, s: str) -> int:
        num = 0
        power = 0

        for i in range(len(s)-1, -1 ,-1):
            if s[i] == '1':
                num += 2 ** power
            power += 1
        
        res = 0
        while num != 1:
            if num & 1:
                num += 1
            else:
                num //= 2
            res += 1

        return res
    
class Solution:
    def numSteps(self, s: str) -> int:
        s = int(s, 2)

        res = 0
        while s != 1:
            if s & 1:
                s += 1
            else:
                s //= 2
            res += 1

        return res