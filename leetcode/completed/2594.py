from typing import List

# r * n^2 = t, where r = rank[i], n = no. of car repaired, t = time needed.
# n = sqrt(t/r),
# here, we want to find minimum t, which satisfies sum(n) >= 'cars'.
# Hence, we can use binary search here.
# Here, the maximum repair time will be min(r) * n^2.

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        lo, hi = 1, min(ranks)*cars*cars

        while lo < hi:
            m = (lo+hi) // 2
            car_repaired = 0
            for rank in ranks:
                car_repaired += int((m//rank)**0.5)
            if car_repaired >= cars:
                hi = m
            else:
                lo = m + 1
        
        return lo
    
# Optimization, as 1 <= ranks[i] <= 100, we can reduce the loop required
# to calculate answer by tracking the count of each unique ranks[i] and calculate the car_repaired at once.

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        lo, hi = 1, min(ranks)*cars*cars
        counter = {}

        for rank in ranks:
            counter[rank] = counter.get(rank, 0) + 1

        while lo < hi:
            m = (lo+hi) // 2
            car_repaired = 0
            for count in counter:
                car_repaired += int((m//count)**0.5) * counter[count]
            if car_repaired >= cars:
                hi = m
            else:
                lo = m + 1
        
        return lo