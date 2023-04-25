class Solution:
    def decodeString(self, s: str) -> str:
        result = ""
        num_stack, char_stack = [] , []
        num_temp = ""
        paren = 0
        for letter in s:
            if letter.isdigit():
                num_temp += letter
            elif letter.isalpha():
                if not char_stack:
                    result += letter
                else:
                    char_stack[-1].append(letter)
            elif letter == '[':
                paren += 1
                num_stack.append(int(num_temp))
                num_temp = ""
                char_stack.append([])
            elif letter == ']':
                paren -= 1
                if not paren:
                    result += "".join(char_stack.pop()) * num_stack.pop()
                else:
                    char_stack[-2].append("".join(char_stack.pop()) * num_stack.pop())

        return result
        
# class Solution:
#     def decodeString(self, s: str) -> str:
#         stack = []
#         num_temp , char_temp = 0 , ""
#         for letter in s:
#             if letter == '[':
#                 stack.append(num_temp)
#                 stack.append(char_temp)
#                 num_temp, char_temp = 0 , ""
#             elif letter == ']':
#                 char_temp = stack.pop() + char_temp*stack.pop()
#             elif letter.isdigit():
#                 num_temp = num_temp * 10 + int(letter)
#             else:
#                 char_temp += letter
#         return char_temp
    
sol = Solution()
s = "2[2[y]xa2[dd]3[z]]"   #"3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
print(sol.decodeString(s))