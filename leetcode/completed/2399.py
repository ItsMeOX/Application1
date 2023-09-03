from typing import List

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        lastSeen = [-1] * 26

        for i in range(len(s)):
            idx = ord(s[i]) - ord('a')
            if lastSeen[idx] != -1 and i-lastSeen[idx]-1 != distance[idx]:
                return False
            lastSeen[idx] = i

        return True