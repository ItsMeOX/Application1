from typing import List

# For each words, group odd and even indexed characters and sort them
# then rebuild the string with the sorted odd and even characters.
# After rebuilding, add the string to a set and the unique string in set will be the res.

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        groups = set()

        for word in words:
            odds = []
            even = []
            for i in range(len(word)):
                if i & 1: odds.append(word[i])
                else: even.append(word[i])
        
            odds.sort()
            even.sort()
            groups.add(''.join(odds) + ''.join(even))


        return len(groups)