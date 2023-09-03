
# Determine swaps needed to make 's' become 10101010.. or 01010101..
# Here I tried to determine the number of numbers that are needed to be swapped.
# If the number is odd, then it is impossible.
# If the length of 's' is odd, then if we want 's' to become 10101, then last digit has to be 1.
#                                                         if 01010, then last digit has to be 0.

class Solution:
    def minSwaps(self, s: str) -> int:
        if abs(s.count('0') - s.count('1')) > 1: return -1

        one_zero = 0
        zero_one = 0
        for i in range(0, len(s)-1, 2):
            if s[i] == '0':
                one_zero += 1
            else:
                zero_one += 1
            if s[i+1] == '1':
                one_zero += 1
            else:
                zero_one += 1

        if len(s) & 1:
            if s[-1] == '0': one_zero += 1
            else: zero_one += 1

        if   not (one_zero & 1 or zero_one & 1): return min(zero_one // 2, one_zero // 2)
        elif one_zero & 1                      : return zero_one // 2
        else                                   : return one_zero // 2

# 1100
# 1001
# 1100
# 0011
# 0110
# 10100