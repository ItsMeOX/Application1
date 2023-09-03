from typing import List

# Sort items by price and beauty, sort queries from low to high.
# i++ if items[i][0] <= query, keep track of the maximum items[i][1] from 0 ~ i.
# Assign cur_max to each correspond index of queries.

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        queries = [(query, i) for i, query in enumerate(queries)]
        queries.sort()
        items.sort()

        res = [0] * len(queries)
        cur_max = 0
        i = 0

        for query, index in queries:
            while i < len(items) and items[i][0] <= query:
                cur_max = max(cur_max, items[i][1])
                i += 1
            res[index] = cur_max
        
        return res