class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_len = len(s1)
        s1_stack = {}   
        for char in s1:
            if char in s1_stack:
                s1_stack[char] += 1
            else:
                s1_stack[char] = 1

        s2_stack = {}
        for char in s2[:s1_len]:
            if char in s2_stack:
                s2_stack[char] += 1
            else:
                s2_stack[char] = 1

        x = 0
        for char in s2[s1_len:]:
            
            if s1_stack == s2_stack:
                return True

            s2_stack[s2[x]] -= 1
            if s2_stack[s2[x]] == 0:
                del s2_stack[s2[x]]
            x += 1



            if char in s2_stack:
                s2_stack[char] += 1
            else:
                s2_stack[char] = 1
            
        if s1_stack == s2_stack:
                return True


        return False

sol = Solution()
s1 , s2 = "a" , "ab"
print(sol.checkInclusion(s1,s2))


# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         from collections import defaultdict

#         s1_len = len(s1)
#         s1_stack = defaultdict(int)   
#         for char in s1:
#             s1_stack[char] += 1

#         s2_stack = defaultdict(int)
#         for char in s2[:s1_len]:
#             s2_stack[char] += 1

#         x = 0
#         for char in s2[s1_len:]:
            
#             if s1_stack == s2_stack:
#                 return True

#             s2_stack[s2[x]] -= 1
#             if s2_stack[s2[x]] == 0:
#                 del s2_stack[s2[x]]
#             x += 1

#             s2_stack[char] += 1

            
#         if s1_stack == s2_stack:
#                 return True


#         return False