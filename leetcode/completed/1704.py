class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left = right = 0

        for i in range(len(s)//2):
            if s[i] in vowels:
                left += 1
            if s[len(s)-i-1] in vowels:
                right += 1
                
        return left == right