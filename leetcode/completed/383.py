class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for c in magazine:
            dic[c] = dic.get(c, 0) + 1

        for c in ransomNote:
            if c not in dic:
                return False
            dic[c] -= 1
            if dic[c] < 0:
                return False

        return True