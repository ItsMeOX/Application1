
# Find frequency of each character in s to 'freq' dictionary.
# Iterate through the values of dictionary and find if they are all the same.

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        t = freq[s[0]]
        for val in freq.values():
            if val != t:
                return False
        
        return True