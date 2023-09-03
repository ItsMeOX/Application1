class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        condition = { # (Bulky, Heavy)
            (0, 0): 'Neither',
            (1, 1): 'Both',
            (1, 0): 'Bulky',
            (0, 1): 'Heavy',
        }

        return condition[(
            length*width*height>=10**9 or any(x>=10**4 for x in [length, width, height]), 
            mass >= 100
        )]