from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        
        for num in range(left, right + 1):
            isValid = True
            num_str = str(num)
            if '0' in num_str: continue
            for i in num_str:
                if num % int(i) != 0:
                    isValid = False
                    break
            if isValid: res.append(num)

        return res