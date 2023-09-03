#     1 2 3 4 5
#    ----------
# 1 | 1 1 1 1 1
# 2 | 1 0 1 0 1
# 3 | 1 0 0 0 1
# 4 | 1 0 0 1 1
# 5 | 1 0 0 1 0

# After i reaches x, x will never be changed.
# The on or off of a bulb is determined by the number integer divisor it has is odd or even.
# For example, 4 -> (1, 2, 4), so it is on at last.
#              2 -> (1, 2), so it is off at last.
# 
# To get the number of divisors:
# 1 -> (1, 1)
# 2 -> (1, 2)
# 3 -> (1, 3)
# 4 -> (1, 4), (2, 2)
# 5 -> (1, 5)
# 6 -> (1, 6), (2, 3)
# 7 -> (1, 7)
# 8 -> (1, 8), (2, 4)
# 9 -> (1, 9), (3, 3)
# 10 -> (1, 10), (2, 5)
# We can see that only 1, 4, 9 has odd numbers of unique integer divisor.
# Then we can deduce that only the perfect squares has odd number of integer divisor.
#
# So, for any number n, we have to loop i from 1 to n,
# and res++ for every i*i <= n.
# To find i, we can just take the rounded down square root of n. 

class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n ** (0.5))