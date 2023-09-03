from typing import List

# Count number of times of appearance in tops and bottoms for each number from 1 to 6.
# Also count if the number of distinct position each number is == len(tops or bottoms),
# if true then we take min(flip to top, flip to bottom) of operations needed for each number and update it to res. 

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        top_cnt = [0] * 8
        bot_cnt = [0] * 8
        valid = [0] * 8

        for t, b in zip(tops, bottoms):
            top_cnt[t] += 1
            bot_cnt[b] += 1
            valid[t] += 1
            if t != b:
                valid[b] += 1

        res = float('inf')
        for i in range(1, 7):
            if valid[i] == len(tops):        
                res = min(len(tops)-top_cnt[i], len(tops)-bot_cnt[i])
        
        return res if res < float('inf') else -1
