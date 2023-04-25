class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        idx = 0
        f_len = len(flowerbed)
        while idx < f_len:
            if flowerbed[idx] != 0:
                idx += 2
                continue
            if idx + 1 < f_len:
                if flowerbed[idx+1] != 0:
                    idx += 3 
                    continue
            n -= 1
            idx += 2

        return n <= 0