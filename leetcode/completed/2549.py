
# For even number n, 
# the number i that are 1 <= i <= n and n%i == 1 will only be n-1.
# For example: 4%3 = 1, there is no other cases.

# For odd number n,
# the number i that are 1 <= i <= and n%i == 1 will only be 2 and n-1.
# For example: 5%4 = 1 and 5%2 = 1.

# So for every number n > 1, return n-1.
#    for every number n <= 1, return 1.

class Solution:
    def distinctIntegers(self, n: int) -> int:
        if n <= 2: return 1
        return n - 1