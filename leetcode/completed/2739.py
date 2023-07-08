class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        res = 0
        while mainTank >= 5:
            mainTank -= 5
            res += 50
            if additionalTank > 0:
                additionalTank -= 1
                mainTank += 1
        res += mainTank * 10
        return res

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int: # list out the numbers of mainTank added from additionalTank and find the sequence
        # litre add->main
        #  5       1
        #  9       2
        #  13      3
        #  y   =  4x + 1
        return (10*(mainTank + min(additionalTank, (mainTank-1)//4)))