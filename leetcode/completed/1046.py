# class Solution:
#     def lastStoneWeight(self, stones: list[int]) -> int:       
#         self.res = 0 
#         self.stop = False
#         def sort(i):
#             if (x:=(i-1)//2) > -1:
#                 if stones[x] < stones[i]:
#                     stones[x] , stones[i] = stones[i] , stones[x]
#                     sort(x)

#         def breakStone():
#             if len(stones) == 1:
#                 self.res = stones[0]
#                 self.stop = True
#                 return
#             if len(stones) == 2:
#                 self.res = stones[0] - stones[1]
#                 self.stop = True 
#                 return
#             if stones[1] > stones[2]:
#                 stones[0] -= stones[1]
#                 stones[1] = stones[-1]
#             else:
#                 stones[0] -= stones[2]
#                 stones[2] = stones[-1]
#             stones.pop()
#             heapify()
            
            
            


#         def heapify():
#             for i in range(len(stones))[1:]:
#                 sort(i)

#         heapify()

#         while not self.stop:
#             breakStone()
        
       
#         return self.res


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        import heapq
        for i, stone in enumerate(stones):
            stones[i] = -stone

        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = -heapq.heappop(stones)
            stone2 = -heapq.heappop(stones)
            if stone1 - stone2:
                heapq.heappush(stones, stone2 - stone1)
        
        if not stones:
            return 0
        else:
            return -stones[0]


sol = Solution()
arr = [7,6,7,6,9]
print(sol.lastStoneWeight(arr))