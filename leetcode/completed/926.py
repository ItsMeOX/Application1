
# Use prefix sum and keep track of one at left and at right,
# For every index i,
# we will split s to s[:i+1] and s[i+1:],
# the total operation needed to make s valid will be 
# one_left + (s_length - i - one_right - 1).
# Compare the operations needed with 'res' every iteration.
# Remember to compare not splitting 's', which is s_length - one_right.

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        one_right = s.count('1')
        one_left = 0

        if one_right == 0 or one_right == len(s): return 0

        res = len(s) - one_right

        for i in range(len(s)):
            c = s[i]
            if c == '1':
                one_right -= 1
                one_left += 1
            res = min(res, one_left+len(s)-i-one_right-1)

        return res