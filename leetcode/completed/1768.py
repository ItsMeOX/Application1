class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        l1, l2 = len(word1), len(word2)

        for i in range(min(l1, l2)):
            res += word1[i]
            res += word2[i]

        return res + word1[l2:] + word2[l1:]
            
            