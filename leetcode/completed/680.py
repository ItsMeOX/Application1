
# If two s[left] and s[right] are different, check if
# 1. remove s[left] and remaining string is palindrome,
# 2. remove s[right] and remaining string is palindrome,
# return True if remaining is palindrome else False, as we cannot remove the character for two times.
# If s[left] == s[right], left += 1, right -= 1.
# return True if the string itself is palindrome.

# Not efficient because of function call stack.
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        def dfs(left, right, error):
            if error > 1: 
                return False
            
            if left >= right:
                return error <= 1

            if s[left] == s[right]:
                return dfs(left+1, right-1, error)
            else:
                return dfs(left+1, right, error+1) or dfs(left, right-1, error+1)
        
        return dfs(left, right, 0)
    
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        def dfs(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return dfs(left+1, right) or dfs(left, right-1)

        return True
    
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                str1 = s[:left]+s[left+1:]
                str2 = s[:right]+s[right+1:]
                return str1 == str1[::-1] or str2 == str2[::-1]

        return True