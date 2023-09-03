from typing import List

# Cumulate shifts from back to front first.
# For every indices i from 0 to len(shifts)-1,
# new_th = (ith alpha + shift) % 26,
# new_ord = new_th + 97.
# (String append will be slower than array.)

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s = list(s)

        for i in range(len(shifts)-2, -1, -1):
            shifts[i] += shifts[i+1]

        for i in range(len(shifts)):
            shift = shifts[i]

            new_ord = (ord(s[i]) - ord('a') + shift) % 26 + 97
            s[i] = chr(new_ord)
        
        return ''.join(s)