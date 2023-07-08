class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1_int = 0
        num2_int = 0

        for d in num1:
            num1_int += ord(d) - ord('1') + 1
            num1_int *= 10
        
        for d in num2:
            num2_int += ord(d) - ord('1') + 1
            num2_int *= 10
        
        return str(num1_int * num2_int // 100)