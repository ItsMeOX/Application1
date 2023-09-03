
# If we encounter n[i] < n[i-1],
# 1. set all the elements from i to end to 9
# 2. iterate from i to 0, if n[i] < n[i-1], decrease n[i-1] by 1, set n[i] to 9.

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n <= 9: return n

        n = list(str(n))

        for i in range(1, len(n)):
            if int(n[i]) < int(n[i-1]):
                n[i+1:] = ['9']*(len(n)-i-1)
                while i > 0 and int(n[i]) < int(n[i-1]):
                    n[i] = '9'
                    n[i-1] = str(int(n[i-1])-1)
                    i -= 1
                break
        return int(''.join(n))
    
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n <= 9: return n

        n = list(str(n))


        for i in range(len(n)-1, 0, -1):
            if int(n[i]) < int(n[i-1]):
                n[i:] = ['9']*(len(n)-i)
                n[i-1] = str(int(n[i-1])-1)
        return int(''.join(n))