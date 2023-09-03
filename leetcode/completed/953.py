from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        indices = {}
        for i in range(len(order)):
            indices[order[i]] = i

        for i in range(1, len(words)):
            min_len = min(len(words[i-1]), len(words[i]))
            if words[i][:min_len] == words[i-1][:min_len]:
                if len(words[i-1]) > len(words[i]):
                    return False
            else:
                for j in range(min_len):
                    if indices[words[i][j]] > indices[words[i-1][j]]:
                        break
                    if indices[words[i][j]] < indices[words[i-1][j]]:
                        return False
            
        return True

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        indices = {}
        for i in range(len(order)):
            indices[order[i]] = i

        for i in range(1, len(words)):
            sorted_flag = False
            for j in range(min(len(words[i-1]), len(words[i]))):
                if indices[words[i][j]] > indices[words[i-1][j]]:
                    sorted_flag = True
                    break
                if indices[words[i][j]] < indices[words[i-1][j]]:
                    return False
            if not sorted_flag and len(words[i-1]) > len(words[i]):
                return False

        return True
    
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        indices = {}
        for i in range(len(order)):
            indices[order[i]] = i

        for i in range(1, len(words)):
            w1, w2 = words[i-1], words[i]
            for j in range(len(w1)):

                if j == len(w2):
                    return False

                if indices[w2[j]] > indices[w1[j]]:
                    break

                if indices[words[i][j]] < indices[words[i-1][j]]:
                    return False

        return True