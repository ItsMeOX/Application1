from heapq import heappush, heappop

# Group digits by odd and even and sort the digits from large to small.
# Also record if num[i] is odd or even ('isOdd' here).
# Then iterate through 'isOdd', if num[i] is odd then add largest odd number else add largest even number to 'res'.
# Note that we cannot use can only use number for num.count(number) time.
# The last res will be the ans.

class Solution:
    def largestInteger(self, num: int) -> int:
        odds = []
        evens = []
        isOdd = []
        while num:
            digit = num % 10
            if digit & 1:
                isOdd.append(True)
                heappush(odds, -digit)
            else:
                isOdd.append(False)
                heappush(evens, -digit)
            num //= 10
        
        isOdd.reverse()
        res = 0
        for odd in isOdd:
            if odd:
                res = res * 10 - heappop(odds)
            else:
                res = res * 10 - heappop(evens)
        
        return res

        