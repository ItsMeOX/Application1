class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits[-1] += 1
        if digits[-1] == 10:
            for i in range(len(digits)-1, 0, -1):
                if digits[i] == 10:
                    digits[i-1] += 1
                    digits[i] = 0
                else:
                    break
            if digits[0] == 10:
                digits[0] = 0
                return [1] + digits
            else:
                return digits
        else:
            return digits
        
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[-1] == 9:
            if len(digits) == 1:
                return [1,0]
            return self.plusOne(digits[:-1]) + [0]
        else:
            digits[-1] += 1
        return digits