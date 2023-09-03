
# Initialize arr with length of atleast 2 to n+1.
# If n is even, for ex: 8, then max i will be 4.
# If n is odd , for ex: 5, then max i will be 3.
# So, n+1 length of arr will be valid. ( arr[0 ~ n] )
# Also, if 2*i+1 is larger than n, we will also just skip it.


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if not n: return 0
        
        arr = [0] * (max(2, n+1))
        arr[1] = 1

        for i in range(n//2+1):
            arr[i*2] = arr[i]
            if 2*i+1 <= n:
                arr[2*i+1] = arr[i] + arr[i+1]

        return max(arr)