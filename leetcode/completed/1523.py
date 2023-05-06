class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return -(-high//2) - -(-low//2) + low%2  #ceil(high/2) - ceil(low/2) + low%2
    

# class Solution:
#     def countOdds(self, low: int, high: int) -> int:
#         if low % 2 == 0:
#             return (high-low+1)//2
#         return (high-low)//2 + 1