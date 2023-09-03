from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counter = {
            5: 0,
            10: 0,
            20: 0
        }
        
        for b in bills:
            counter[b] += 1
            if b == 10: 
                if not counter[5]:
                    return False
                counter[5] -= 1
            elif b == 20:
                if counter[10] and counter[5]:
                    counter[10] -= 1
                    counter[5] -= 1
                elif counter[5] > 2:
                    counter[5] -= 3
                else:
                    return False
            
        return True