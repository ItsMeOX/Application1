
# Create counter for array 'a' and 'b' and count the frequency of alphabets for each array.
# We iterate from 0 to 26 (a~z) and for each alphabet
# we have to check for 3 cases:
# 1. number of operation needed to change all other alphabets to current alphabets for array 'a' and 'b'.
# 2. number of operation needed to change alphabets larger than current alphabet for array 'a' to current alphabet.
#    +
#    number of operation needed to change alphabets smaller and equal to current alphabet for array 'b'.
# 3. same as (2) but swap array 'a' and 'b'.
# (we have to take care of alphabet z as z is not valid for case (2) and (3)).

class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        counter_a = [0] * 26
        counter_b = [0] * 26

        for c in a:
            counter_a[ord(c)-ord('a')] += 1
        for c in b:
            counter_b[ord(c)-ord('a')] += 1

        res = float('inf')
        sum_a, sum_b = sum(counter_a), sum(counter_b)
        pre_a, pre_b = 0, 0

        for i in range(26):
            pre_a += counter_a[i]
            pre_b += counter_b[i]

            res = min(res, sum_a + sum_b - counter_a[i] - counter_b[i])

            if i == 25: break

            to_a = sum_a - pre_a + pre_b
            to_b = sum_b - pre_b + pre_a

            res = min(res, to_a)
            res = min(res, to_b)

        return res