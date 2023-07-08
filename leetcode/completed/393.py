from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def getLeadingOnes(num):
            mask = 128
            cnt = 0
            while mask > 0:
                if num & mask != 0:
                    cnt += 1
                    mask //= 2
                else:
                    return cnt                
            return cnt

        i = 0
        while i < len(data):
            leadingOnes = getLeadingOnes(data[i])
            if leadingOnes == 1 or leadingOnes > 4: return False
            for _ in range(1, leadingOnes):
                i += 1
                if i >= len(data) or getLeadingOnes(data[i]) != 1:
                    return False
            i += 1
        return True