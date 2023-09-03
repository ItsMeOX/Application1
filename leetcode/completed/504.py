
# Just treat this like convertToBase10, except that base is 7 instead of 10.

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num < 0:
            symbol = '-'
            num = -num
        elif num > 0:
            symbol = ''
        else:
            return '0' # remember to take care of 0.

        res = ''
        while num:
            res += str(num%7)
            num //= 7
        
        return symbol + res[::-1]