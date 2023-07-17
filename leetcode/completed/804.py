from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mapping = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        pattern = set()

        res = 0
        for word in words:
            cur_pattern = ''
            for c in word:
                cur_pattern += mapping[ord(c)-ord('a')]
            if cur_pattern not in pattern:
                res += 1
                pattern.add(cur_pattern)

        return res