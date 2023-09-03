from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = w2 = ''

        for c in word1:
            w1 += c
        for c in word2:
            w2 += c
        
        return w1 == w2
    
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)