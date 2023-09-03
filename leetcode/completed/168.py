class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        while columnNumber:
            if columnNumber <= 26:
                res += chr(columnNumber + ord('A') - 1)
                return res[::-1]
            columnNumber -= 1
            remainder = columnNumber % 26
            columnNumber //= 26
            res += chr(remainder + ord('A'))
    
# (columnNumber - 1) % 26 makes 
# 26 -> Z
# 0 -> A

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        while columnNumber:
            columnNumber -= 1
            res = alpha[columnNumber % 26] + res
            columnNumber //= 26
        
        return res