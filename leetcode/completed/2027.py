
# Just move 2 steps further whenever we see 'X' and increase 'res' by 1 greedily.
# Else just move 1 step further.

class Solution:
    def minimumMoves(self, s: str) -> int:
        i = 0
        res = 0
        while i < len(s):
            if s[i] == 'X':
                res += 1
                i += 2
            i += 1

        return res