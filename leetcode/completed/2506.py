from typing import List

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        sets = []
        res = 0

        for i in range(len(words)):
            cur_set = set(list(words[i]))
            for j in range(i):
                if sets[j] == cur_set:
                    res += 1
            sets.append(cur_set)
        
        return res
    
from collections import defaultdict
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        dic = defaultdict(int)

        for word in words:
            dic[''.join(sorted(set(word)))] += 1

        res = 0
        for val in dic.values():
            res += val * (val-1) // 2
        
        return res
        