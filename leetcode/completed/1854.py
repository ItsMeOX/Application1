from typing import List
from heapq import heappop, heappush

# Sort the logs by the birth year.
# For every born and death year, 
# check in heap if any death year < current born year,
# if true then current population -= 1.
# If current population > max population, update max population and max population year. 
# After done checking, heappush current death year into the min heap.

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        logs.sort()
        max_pop = cur_pop = max_year = 0
        heap = []

        for born, dead in logs:
            while heap and heap[0] <= born:
                heappop(heap)
                cur_pop -= 1
            cur_pop += 1
            if cur_pop > max_pop:
                max_pop = cur_pop
                max_year = born
            heappush(heap, dead)
        
        return max_year
    
# Optimization:
# Using line sweep technique, 
# years = [0,0,0...]*(maximum year - minimum year)
# for every born and dead in logs,
# years[born] += 1, years[dead] -= 1.
# Then iterate through 'years' and add years[i] to cur_pop,
# if cur_pop > max_pop, update max_pop and max_year.

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [0] * (2051 - 1950)

        for born, dead in logs:
            years[born-1950] += 1
            years[dead-1950] -= 1
        
        max_year = max_pop = cur_pop = 0

        for i in range(len(years)):
            delta = years[i]
            cur_pop += delta
            if cur_pop > max_pop:
                max_pop = cur_pop
                max_year = i + 1950
        
        return max_year