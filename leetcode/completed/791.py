
# Keep a counter of characters in s.
# Append characters according to order of 'order' to 'res' first, 
# then append all the characters remaining to 'res'.

class Solution:
    def customSortString(self, order: str, s: str) -> str:

        counter = [0] * 26

        for c in s:
            counter[ord(c) - ord('a')] += 1
        
        res = []
        for c in order:
            res.append(c * counter[ord(c) - ord('a')])
            counter[ord(c) - ord('a')] = 0
        
        for i in range(26):
            if counter[i]:
                res.append(chr(ord('a') + i) * counter[i])
        
        return ''.join(res)