from collections import deque

# Because that 'L' and 'R' cannot cross each other, 
# we firstly have to make sure that the relative position of 'L' and 'R' in start and end are the same,
# if the relative position are not the same, then return False.
# Then, for example we have 'XXXL' for start, then we know that 'L' index in end must be in [0 ~ 2], as 'L' can only move left.
# Same for 'R', the index of ith 'R' for start must be <= the index of ith 'R' for end.
# If the above three conditions are not broken, then return True otherwise False.

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.replace('X', '') != end.replace('X', ''):
            return False

        Lpos, Rpos = deque(), deque()
        for i in range(len(end)):
            if end[i] == 'L':
                Lpos.append(i)
            elif end[i] == 'R':
                Rpos.append(i)
        
        for i in range(len(start)):
            if start[i] == 'L' and Lpos.popleft() > i:
                return False
            elif start[i] == 'R' and Rpos.popleft() < i:
                return False
        
        return True