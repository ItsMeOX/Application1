
# Any odd number will not have perfect integer.
# For even numbers,
# we set initial sum to 1, as any number is divisible by 1.
# Then we iterate 'i' from 2 to sqrt(num), 
# if num is divisible by 'i', then num/'i' is also divisible by 'i'.
# For example:
# num = 28, i = 4
# as 28 is disvible by 4, 
# then 28/4 is also disivible for 28,
# so we add 28/4 + 4 to sums.
# Finally check if sums is equal to num.

#               ____
#              |   |
#              |   |
# 28 = 1 + 2 + 4 + 7 + 14
#          |            |
#          |            |
#          |____________|

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num % 2:
            return False
        
        sums = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                sums += i + num // i

        return sums == num