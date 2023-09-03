class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set([n])
        while n != 1:
            t = 0
            while n:
                t += (n % 10)**2
                n //= 10
            n = t
            if t in seen: return False
            seen.add(t)

        return True
    
# Similar to Floyd's cycle detection algorithm used in linked list,
# Initialize two pointers 'slow' and 'fast', 
# if they ever meet, that means we have a cycle here.
# check if they are 0 or not, return true if yes else false.
# If fast / slow == 1, return true.

class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(x):
            res = 0
            while x:
                res += (x%10)**2
                x //= 10
            return res
        
        slow, fast = n, next_num(n)

        while slow != fast:
            if fast == 1: return True
            slow = next_num(slow)
            fast = next_num(next_num(fast))
        
        return slow == 1