class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        temp = start ^ goal
        return bin(temp).count('1')