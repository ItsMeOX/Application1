from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        pos = {}
        concatenated = [False] * len(arr)

        for i in range(len(arr)):
            pos[arr[i]] = i

        for piece in pieces:
            if piece[0] not in pos: continue
            if len(piece) == 1:
                concatenated[pos[piece[0]]] = True
            else:
                if concatenated[pos[piece[0]]] == False:
                    fit = True
                    if pos[piece[0]] + len(piece) > len(arr):
                        fit = False
                    else:
                        for i in range(len(piece)):
                            if arr[pos[piece[0]]+i] != piece[i]:
                                fit = False
                                break
                    if fit:
                        for i in range(len(piece)):
                            concatenated[pos[piece[0]]+i] = True

        return all(concatenated)
    

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mapping = {}
        for i in range(len(pieces)):
            mapping[pieces[i][0]] = pieces[i]
        
        res = []
        for num in arr:
            if num in mapping:
                res += mapping[num]

        return res == arr
        
sol = Solution()
print(sol.canFormArray([49, 18, 16], [[16], [16,18,49], [18], [49]]))