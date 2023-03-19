class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1
        
        first , sec , third  = 0 , 1 , 1 

        for _ in range(n-2):
            temp = first + sec + third
            first = sec
            sec = third
            third = temp

        return third
