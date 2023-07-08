from typing import List

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        words.sort(key = lambda e: len(e))

        cnt = {}

        for word in words:
            cnt = {}            
            for c in licensePlate:
                if c.isalpha():
                    c = c.lower()
                    cnt[c] = cnt.get(c, 0) + 1
            for c in word:
                if c in cnt:
                    cnt[c] -= 1
                    if cnt[c] == 0:
                        del cnt[c]
            if not cnt:
                return word