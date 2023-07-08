from typing import List

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt = {}
        cnt2 = {}
        res = 0

        for w in words1:
            cnt[w] = cnt.get(w, 0) + 1
        
        for w in words2:
            cnt2[w] = cnt2.get(w, 0) + 1

        for w in cnt.keys():
            if w in cnt2 and cnt[w] == 1 and cnt2[w] == 1:
                res += 1

        return res
            