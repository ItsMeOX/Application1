# My approach:
# Create a coordinate (x, y) for each alphabets.
# Add an 'a' infront of target, and we will iterate alphabets and get dx and dy, 
# from dx and dy, we print how many steps to walk.
# Also, there is a specific priority for walking:
# 1. up
# 2. left
# 3. right = down

# Examples unexpected: "zdz"
#                      "zb"

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        pos = {}
        for i in range(5):
            for j in range(5):
                pos[chr(ord('a')+5*i+j)] = (i, j)
        pos['z'] = (5, 0)

        target = 'a' + target
        res = ''

        for i in range(1, len(target)):
            y1, x1 = pos[target[i-1]]
            y2, x2 = pos[target[i]]

            
            if y2-y1 < 0:
                res += 'U'*(y1-y2)
            if x2-x1 < 0:
                res += 'L'*(x1-x2)
            if x2-x1 > 0:
                res += 'R'*(x2-x1)
            if y2-y1 > 0:
                res += 'D'*(y2-y1)

            res += '!'

        return res
    
# Here instead of precalculating all the coordinates of alphabets,
# we can also calculate it only when we needed.

# %5 =>  0, 1, 2, 3, 4
#        0, 1, 2, 3, 4
#        ...

# //5 => 0, 0, 0, 0, 0
#        1, 1, 1, 1, 1
#        ...

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        res = ''
        x, y = 0, 0

        for c in target:
            cur_x = (ord(c) - ord('a'))  % 5
            cur_y = (ord(c) - ord('a')) // 5

            dy = cur_y - y
            dx = cur_x - x

            if dy < 0:
                res += 'U' * -dy
            if dx < 0:
                res += 'L' * -dx
            if dx > 0:
                res += 'R' * dx
            if dy > 0:
                res += 'D' * dy
            
            res += '!'

            x, y = cur_x, cur_y
        
        return res