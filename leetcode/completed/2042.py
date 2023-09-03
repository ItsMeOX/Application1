class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        cur_num = 0
        digits = '0123456789'

        for phrase in s.split(' '):
            if phrase[0] in digits: 
                if int(phrase) <= cur_num:
                    return False
                cur_num = int(phrase)

        return True