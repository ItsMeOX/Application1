
# Count the number of continuous same alphabets.
# The substrings it can form will be like:
# a 
# aa
# aaa
# aaaa
# aaaaa
# aaaaaa
# it will be in form: 
# 1 + 2 + 3 + 4 + 5 + 6
# = (1+6) + (2+5) + (3+4)
# = 7 + 7 + 7
# = (6+1) + (6+1) + (6+1)
# = (6+1) * (6 // 2)
# = (n+1)*n // 2
# Calculate (n+1) * n // 2 for each interval and add it to res.
# (dunno how to prove for odd number)

class Solution:
    def countHomogenous(self, s: str) -> int:
        res = 0
        last_c = s[0]
        last_c_count = 0
        MOD = 10 ** 9 + 7

        for c in s:
            if c == last_c:
                last_c_count += 1
            else:
                last_c = c
                res += (last_c_count+1) * last_c_count // 2
                last_c_count = 1

        return (res + (last_c_count+1) * last_c_count // 2) % MOD