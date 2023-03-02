# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if not s:
#             return 0
        
#         left , right , s_len = 0 , 1 , len(s)
#         visited , max_len = [s[0]] , 0

#         while True:
#             while right < s_len and s[right] not in visited:
#                 visited.append(s[right])
#                 right += 1
#             else:
#                 if right - left > max_len:
#                     max_len = right - left
#                 if left < s_len - 1:
#                     left += 1
#                     right = left + 1
#                     visited = [s[left]]
#                 else:
#                     break
        
#         return max_len

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        max_len = 0
        left = 0

        for right , char in enumerate(s):
            if char in visited and visited[char] >= left:
                left = visited[char] + 1
            visited[char] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len



sol = Solution()
word = "bbtablud"
print(sol.lengthOfLongestSubstring(word))
