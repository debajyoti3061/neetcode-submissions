# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

"""
REVISION NOTES - Guess Number Higher Or Lower:
• Classic binary search problem using provided guess API
• Use two pointers (left, right) to define search range
• Calculate middle point and call guess() to get feedback
• Adjust search range based on API response: 1 (too low), -1 (too high), 0 (correct)
• Continue until correct number is found
• Time: O(log n), Space: O(1)
"""

class Solution:
    def guessNumber(self, n: int) -> int:
        l , r = 1, n
        while True:
            m = (l+r)//2
            result = guess(m)
            if result == 1:
                l = m+1 
            elif result  == -1:
                r = m-1
            else :
                return m

        