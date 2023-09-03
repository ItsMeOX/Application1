from typing import List

# Starting from i = 0,
# if bits[i] == 1, then we must take bits[i+1] also, so i + 2
# if bits[i] == 0, then we can only take current bit, so continue to bits[i+1], so i + 1.
# if i lands at len(bits)-1, that means that bits[-1] can be one-bit character,
# else if i cannot land at len(bits)-1, then bits[-1] cannot be one-bit character.

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits):
            if i == len(bits) - 1:
                return True
            if bits[i] == 1:
                i += 2
            else:
                i += 1
            
        return False