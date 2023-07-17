class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles

        while numBottles > numExchange-1:
            mod = numBottles % numExchange
            numBottles //= numExchange
            res += numBottles
            numBottles += mod
        
        return res
            