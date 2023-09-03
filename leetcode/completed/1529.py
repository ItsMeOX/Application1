class Solution:
    def minFlips(self, target: str) -> int:
        cur_bit = '0'
        res = 0

        for bit in target:
            if cur_bit != bit:
                res += 1
                cur_bit = bit
        
        return res