
# idk 2.

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if len(sentence1) > len(sentence2):
            sentence1, sentence2 = sentence2, sentence1

        sentence1 = sentence1.split(' ')
        sentence2 = sentence2.split(' ')

        left = right = 0

        while left < len(sentence1):
            if sentence1[left] == sentence2[right]:
                left += 1
                right += 1
            else:
                while sentence1[left] != sentence2[right]:
                    right += 1
                    if right == len(sentence2): return False
                if sentence1[left:] == sentence2[right:]: return True
                break
        
        left = len(sentence1)-1
        right = len(sentence2)-1
        while left >= 0:
            if sentence1[left] == sentence2[right]:
                left -= 1
                right -= 1
            else:
                while sentence1[left] != sentence2[right]:
                    right -= 1
                    if right == -1: return False
                print(sentence1[:left], sentence2[:right])
                if sentence1[:left] != sentence2[:right]: return False

        return True

from collections import deque
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        q1 = deque(list(sentence1.split(' ')))
        q2 = deque(list(sentence2.split(' ')))

        while q1 and q2 and q1[0] == q2[0]:
            q1.popleft()
            q2.popleft()

        while q1 and q2 and q1[-1] == q2[-1]:
            q1.pop()
            q2.pop()

        return not q1 or not q2