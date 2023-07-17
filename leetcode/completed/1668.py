class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        temp = 0
        res = 0

        for i in range(len(sequence)):
            temp = 0
            for j in range(i, len(sequence), len(word)):
                if sequence[j:j+len(word)] == word:
                    temp += 1
                else:
                    res = max(res, temp)
                    temp = 0
        
            res = max(res, temp)

        return res
    
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        res = 0

        while word * res in sequence:
            res += 1
        
        return res - 1