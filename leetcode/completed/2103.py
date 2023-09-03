class Solution:
    def countPoints(self, rings: str) -> int:
        rods = {}
        res = 0
        for i in range(0, len(rings), 2):
            color = rings[i]
            rod   = rings[i+1]
            if rod in rods and color in rods[rod]:
                continue
            rods[rod] = rods.get(rod, '') + color
            if len(rods[rod]) == 3: res += 1

        return res
    
class Solution:
    def countPoints(self, rings: str) -> int:
        res = 0
        for i in range(10):
            i = str(i)
            if 'R' + i in rings and 'G' + i in rings and 'B' + i in rings:
                res += 1

        return res