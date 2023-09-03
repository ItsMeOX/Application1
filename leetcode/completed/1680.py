class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = ''
        MOD = 10 ** 9 + 7

        for i in range(1, n+1):
            res += bin(i)[2:]

        return int(res, 2) % MOD
    
# Iterate from 1 to n.
# If n meets power ('power') of two, then we have to increase the bit length ('length') by 1 and update 'power' to next power of 2.
# On every iteration, we push res left 'length' bits and bitwise_OR 'res'.
# For example:
# i=0: 0
# i=1: 00 | 01 = 01
# i=2: 0100 | 0010 = 0110

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        power = 1
        length = 0
        res = 0
        MOD = 10 ** 9 + 7

        for i in range(1, n+1):
            if i == power:
                power <<= 1
                length += 1
            res = ((res << length) | i) % MOD
        
        return res
    
sol = Solution()
print(sol.concatenatedBinary(2))