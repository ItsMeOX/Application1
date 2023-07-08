class Solution:
    def checkRecord(self, s: str) -> bool:
        return False if 'LLL' in s or s.count('A') >= 2 else True
    
class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        for i in range(len(s)):
            if s[i] == 'A':
                absent += 1
            elif s[i:i+3] == 'LLL':
                return False

        return True if absent < 2 else False