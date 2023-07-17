from bisect import bisect_right

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d_idx = []
        r_idx = []
        banned = [False] * len(senate)

        for i in range(len(senate)):
            if senate[i] == 'R':
                r_idx.append(i)
            else:
                d_idx.append(i)

        i = 0
        while d_idx and r_idx:
            if not banned[i]:
                if senate[i] == 'R':
                    idx = bisect_right(d_idx, i)
                    if idx == len(d_idx): idx = 0
                    banned[d_idx[idx]] = True
                    d_idx.pop(idx)
                else:
                    idx = bisect_right(r_idx, i)
                    if idx == len(r_idx): idx = 0
                    banned[r_idx[idx]] = True
                    r_idx.pop(idx)
            i += 1
            if i == len(senate): i = 0

        return 'Radiant' if r_idx else 'Dire'
    
from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d_idx = deque()
        r_idx = deque()

        for i in range(len(senate)):
            if senate[i] == 'R':
                r_idx.append(i)
            else:
                d_idx.append(i)

        while d_idx and r_idx:
            dire = d_idx.popleft()
            radiant = r_idx.popleft()

            if dire > radiant:
                r_idx.append(radiant + len(senate))
            else:
                d_idx.append(dire + len(senate))

        return 'Radiant' if r_idx else 'Dire'