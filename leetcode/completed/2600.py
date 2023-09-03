class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        res = min(k, numOnes)

        k -= res

        k -= min(k, numZeros)

        res -= k

        return res