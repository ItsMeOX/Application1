from typing import List

# No matter how we walk, we will eventually walk through all of the rows and grids between us and the home.
# So, just greedily sum up costs between us and homePos.

class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        sr, sc = startPos
        tr, tc = homePos

        if sr < tr:
            row_cost = sum(rowCosts[sr+1: tr+1])
        else:
            row_cost = sum(rowCosts[tr: sr])
        
        if sc < tc:
            col_cost = sum(colCosts[sc+1: tc+1])
        else:
            col_cost = sum(colCosts[tc: sc])

        return col_cost + row_cost