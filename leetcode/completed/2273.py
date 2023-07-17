from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        toBeRemoved = set()
        counter = []

        for word in words:
            count = {}
            for c in word:
                count[c] = count.get(c, 0) + 1
            counter.append(count)

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if i not in toBeRemoved and j not in toBeRemoved and i != j:
                    if counter[i] == counter[j]:
                        toBeRemoved.add(j)
                    else:
                        break
                else:
                    break
        
        res = []
        for i in range(len(words)):
            if i not in toBeRemoved:
                res.append(words[i])
        
        return res
    
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]

        for i in range(1, len(words)):
            if sorted(words[i]) != sorted(res[-1]):
                res.append(words[i])
        
        return res