
# String that has leading zero or more than one consecutive one will have
# the substring '01'.
# 0000011
# 1011111

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return '01' not in s