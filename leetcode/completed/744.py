class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str: # O(logn)
        target_lex = ord(target)
        l, r = 0, len(letters)-1

        while l < r:
            m = (l+r) // 2
            m_lex = ord(letters[m])
            if m_lex <= target_lex:
                l = m + 1
            else:
                r = m
        
        if l == len(letters)-1 and ord(letters[l]) <= target_lex:
            return letters[0]
        return letters[l]
            
class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str: # O(n)
        target_lex = ord(target)
        for letter in letters:
            if ord(letter) > target_lex:
                return letter

        return letters[0]