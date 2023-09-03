# Use hash set to record travelled coordinates.

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        visited.add((0, 0))
        x, y = 0, 0
        directions = {
            'N': (0 ,  1),
            'S': (0 , -1),
            'E': (1 ,  0),
            'W': (-1,  0),
        }

        for d in path:
            dx, dy = directions[d]
            x += dx
            y += dy
            if (x, y) in visited:
                return True
            visited.add((x, y))

        return False