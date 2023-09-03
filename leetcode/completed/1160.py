from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        counter = {}
        for c in chars:
            counter[c] = counter.get(c, 0) + 1
        
        for word in words:
            temp = {}
            for char in word:
                temp[char] = temp.get(char, 0) + 1
            for key in temp:
                if key not in counter or temp[key] > counter[key]:
                    break
            else:
                res += len(word)

        return res
    
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        
        for word in words:
            for char in word:
                if word.count(char) > chars.count(char):
                    break
            else:
                res += len(word)

        return res