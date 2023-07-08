from typing import List

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        cnt = [word.count(min(word)) for word in words]
        freqs = [0] * (max(cnt)+1)

        for c in cnt:
            freqs[c] += 1
        
        for i in range(len(freqs)-2, -1, -1):
            freqs[i] += freqs[i+1]

        res = [0] * len(queries)

        for i in range(len(queries)):
            freq = queries[i].count(min(queries[i]))+1
            if freq < len(freqs):
                res[i] = freqs[freq]
            else:
                res[i] = 0

        return res