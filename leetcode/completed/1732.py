class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        att = res = 0
        for g in gain:
            att += g
            res = max(res, att)

        return res