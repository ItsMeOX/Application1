class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        counter = {}

        for c in word1:
            counter[c] = counter.get(c, 0) + 1

        for c in word2:
            counter[c] = counter.get(c, 0) - 1

        for val in counter.values():
            if abs(val) > 3:
                return False

        return True
    
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        counter = {}

        for i in range(len(word1)):
            counter[word1[i]] = counter.get(word1[i], 0) + 1
            counter[word2[i]] = counter.get(word2[i], 0) - 1

        for val in counter.values():
            if abs(val) > 3:
                return False

        return True