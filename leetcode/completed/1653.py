class Solution:
    def minimumDeletions(self, s: str) -> int:
        pref_a = [0 if s[-1] == 'b' else 1]
        pref_b = [0 if s[0] == 'a' else 1] # b before, a after

        for i in range(1, len(s)):
            pref_b.append(pref_b[-1] + int(s[i] == 'b'))

        for i in range(len(s)-2, -1, -1):
            pref_a.append(pref_a[-1] + int(s[i] == 'a'))
        pref_a.reverse()

        res = float('inf')
        for i in range(1, len(s)-1):
            res = min(res, pref_b[i-1] + pref_a[i+1])

        return min(res, s.count('b'), s.count('a'))
    
# Because we know that 'b' cannot come before 'a',
# we can count how many pairs of 'ba' there are in the string.
# The final count will be the least amount of deletion we need.

class Solution:
    def minimumDeletions(self, s: str) -> int:
        stk = []
        res = 0

        for c in s:
            if stk and c == 'a' and stk[-1] == 'b':
                res += 1
                stk.pop()
            else:
                stk.append(c)

        return res