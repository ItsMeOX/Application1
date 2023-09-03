
# Keep a sliding window of size k, and keep track of the amount of 'W' in the window.
# If the size of the window (right + 1) >= k, then compare current count of 'W' with res, and update res with the smaller one,
# then decrease the size of the window by increasing the left pointer of window by 1.
# Remember to decrease 'cnt' by one if the left of window is 'W'.
# (right + 1) >= k, I originally wrote (if right - left + 1 >= k).

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = float('inf')
        left = 0
        cnt = 0

        for right in range(len(blocks)):
            if blocks[right] == 'W':
                cnt += 1
            if right+1 >= k:
                res = min(res, cnt)
                if blocks[left] == 'W': # can replace left with right-k+1
                    cnt -= 1
                left += 1
        
        return res