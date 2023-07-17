from typing import List

# let x = candy swapped by Bob, 
#     y = candy swapped by Alice
#     Sa = sum of candy of Alice
#     Sb = sum of candy of Bob

# for the two to have same amount of candy,
# we have the equation:
# Sa + x - y = Sb - x + y
# Sa + Sb = 2(y-x)
# (Sa + Sb) / 2 = y - x
# y = (Sa + Sb) / 2 + x

# so if (Sa + Sb) / 2 + bobsize is in aliceSizes,
# there will be a solution.

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceSum = sum(aliceSizes)
        bobSum = sum(bobSizes)
        difference = (aliceSum - bobSum) // 2

        aliceSet = set(aliceSizes)
        for size in bobSizes:
            if size + difference in aliceSet:
                return [size+difference, size]