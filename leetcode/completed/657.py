class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dx = dy = 0
        for move in moves:
            if move == 'U': dy -= 1
            elif move == 'D': dy += 1
            elif move == 'L': dx -= 1
            else: dx += 1
        
        return dx == dy == 0

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')