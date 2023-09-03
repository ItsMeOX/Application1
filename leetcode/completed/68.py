from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        spaces = []
        word = []
        cur_len = 0

        for i in range(len(words)):
            word.append(words[i])
            cur_len += len(words[i])

            spaces.append(' ')
            cur_len += 1

            if i == len(words) - 1:
                break
            if cur_len + len(words[i+1]) > maxWidth:
                if len(word) > 1:
                    spaces.pop()
                    cur_len -= 1
                space_remain = maxWidth - cur_len
                if space_remain < 0:
                    spaces.clear()

                temp = ''
                for j in range(space_remain):
                    spaces[j%len(spaces)] += ' '
                for j in range(len(word)):
                    temp += word[j]
                    if j < len(spaces):
                        temp += spaces[j]
                res.append(temp)
                cur_len = 0
                word.clear()
                spaces.clear()
        
        res.append(' '.join(word))
        res[-1] += ' ' * (maxWidth - len(res[-1]))
        

        return res
    

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        cur_words = []
        cur_len = 0

        for word in words:
            # if length of current words + length of to be added word + length of blanks > maxWidth, justify and append current words.
            if len(word) + cur_len + len(cur_words) > maxWidth:
                for i in range(maxWidth - cur_len):
                    # add blank from 0 to len - 1.
                    cur_words[i%(len(cur_words)-1 or 1)] += ' '
                res.append(''.join(cur_words))
                cur_words, cur_len = [], 0

            cur_words.append(word)
            cur_len += len(word)

        # number of blanks to be added at tail = maxWidth - length of current words - length of blanks (+ 1 because last blank should not be counted.)
        res.append(' '.join(cur_words) + ' ' * (maxWidth - cur_len - len(cur_words) + 1))

        return res