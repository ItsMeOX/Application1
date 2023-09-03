
# Create mask of one two three four,
# then starting from 11111..., append cur_bulb ^ four masks to new set,
# the final length of the set will be total statutes.

class Solution:
    def flipLights(self, n: int, presses: int) -> int:

        one, two, three, four = 0, 0, 0, 0
        for i in range(1, n+1):
            one = (one << 1) + 1
            two = (two << 1) + ((i-1) % 2 == 0)
            three = (three << 1) + ((i-1) % 2 == 1)
            four = (four << 1) + ((i-1) % 3 == 0)
        
        prev = set([one])
        for _ in range(presses):
            cur = set()
            for _ in range(len(prev)):
                bulb = prev.pop()
                for next_bulb in [bulb ^ one, bulb ^ two, bulb ^ three, bulb ^ four]:
                    cur.add(next_bulb)
            prev = cur

        return len(prev)
            