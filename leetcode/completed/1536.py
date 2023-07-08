from typing import List
from collections import defaultdict

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        memo = defaultdict(int) # memo[how many zeroes] = at which row
        for i, row in enumerate(grid): # iterate and find how (how many zeroes) is at (which row)
            cnt = 0
            for j in range(len(row)-1, -1 ,-1): # count zeroes
                if row[j] == 0:
                    cnt += 1
                else:
                    break

            if cnt in memo: # if same amount of zeroes already exists in memo, decrease the amount of zero as backup for others
                while cnt in memo:
                    cnt -= 1
            memo[cnt] = i
        
        res = 0
        for i in range(len(grid)-1, -1, -1): # start from top row, zeroes = len(grid)-1
            cur_row = len(grid)-1-i # len(grid)-1-i = current row
            k = -1 # key of memo that can fit in current row of zeroes
            for key in memo.keys():
                if key >= i and memo[key] >= cur_row: # find only key where memo[key] >= current needed zeroes and row of key need to be at >= current row
                    k = key
                    break
            if k == -1: # if key is -1, that means no row which has zeroes >= current needed zeroes
                return -1
            res += memo[k] - cur_row # number of row swaps needed
            
            # update position between current row and those needed to increase by 1
            for key in memo.keys():
                if memo[key] >= cur_row and memo[key] < memo[k]:
                    memo[key] += 1
            memo[k] = cur_row
        return res
    

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        def countZeroes(i):
            cnt = 0
            for j in range(len(grid[i])-1, -1, -1):
                if grid[i][j] == 0:
                    cnt += 1
                else:
                    break
            return cnt

        zeroes = [countZeroes(i) for i in range(len(grid))]

        res = 0
        for i in range(len(grid)):
            z_needed = len(grid)-1-i
            if zeroes[i] < z_needed:
                possible = False
                for j in range(i+1, len(grid)):
                    if zeroes[j] >= z_needed:
                        possible = True
                        res += (j-i)
                        zeroes[i+1:j+1] = zeroes[i:j]
                        break
                if not possible:
                    return -1

        return res