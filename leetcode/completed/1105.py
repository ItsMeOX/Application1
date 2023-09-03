from typing import List
from functools import cache


# Base case:
# If we reach i == n, remember to count in the maximum height of current (last) row.

# Cases:
# For every index i, we can choose to 
# 1. place current books[i] at current row:
#    To place at current row, we have to make sure that books[i] + curWidth <= shelfWidth,
#    add add current book width to curWidth 
#    and update maxHeight with current book height and maxHeight.
# 2. place current books[i] at next row:
#    we traverse to next book 
#    and update maxHeight to this book 
#    and set curWidth to this book 
#    and + maxHeight of this row to res.

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:

        @cache
        def dfs(i, curWidth, maxHeight):
            if i == len(books):
                return maxHeight
            
            # not place on this row
            res = dfs(i+1, books[i][0], books[i][1]) + maxHeight

            # place on this row
            if curWidth + books[i][0] <= shelfWidth:
                res = min(res, dfs(i+1, curWidth + books[i][0], max(maxHeight, books[i][1])))

            return res
        
        return dfs(0, 0, 0)
    
# one state
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:

        @cache
        def dfs(i):
            if i == len(books):
                return 0

            curWidth = 0
            maxHeight = books[i][1]
            res = float('inf')
            for j in range(i, len(books)):
                if curWidth + books[j][0] > shelfWidth: break
                curWidth += books[j][0]
                maxHeight = max(maxHeight, books[j][1])
                res = min(res, maxHeight + dfs(j+1))

            return res
        
        return dfs(0)
    
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = [float('inf')] * (len(books)+1)
        dp[-1] = 0

        for i in range(len(books)-1, -1, -1):
            curWidth = 0
            maxHeight = books[i][1]
            for j in range(i, len(books)):
                if curWidth + books[j][0] > shelfWidth: break
                curWidth += books[j][0]
                maxHeight = max(maxHeight, books[j][1])
                dp[i] = min(dp[i], maxHeight + dp[j+1])

        return dp[0]