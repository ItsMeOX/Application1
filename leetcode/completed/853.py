from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        time_needed_arr = []
        res = 1

        for p, s in sorted(zip(position, speed), key=lambda e: (-e[0], e[1])):
            time_needed = (target-p) / s
            if time_needed_arr:
                if time_needed > time_needed_arr[-1]:
                    res += 1
                    time_needed_arr.append(time_needed)
            else:
                time_needed_arr.append(time_needed)

        return res

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        indices = [i for i in range(len(position))]
        indices.sort(key = lambda e: -position[e])
        max_time_needed = -1
        res = 0

        for i in indices:
            time_needed = (target-position[i]) / speed[i]
            if time_needed > max_time_needed:
                res += 1
                max_time_needed = time_needed

        return res
