class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split(" ")
        i = len(x)-1
        while not x[i]:
            i -= 1
        return len(x[i])