from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(bin(i).count('1'))

        return res
    
# Divide by 1 => right shift by 1,
# if i is odd, the last digit will be 1 otherwise 0, and the 0 ~ n-1 digits will be the same as
# of n / 2 .

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n+1):
            res.append(res[i//2] + (i & 1))

        return res