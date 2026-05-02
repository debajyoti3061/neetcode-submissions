"""
REVISION NOTES - Non-Cyclical Number (Happy Number):
• Use set to detect cycles in the sum of squares sequence
• Keep computing sum of squares of digits until reaching 1 or detecting cycle
• If we reach 1, number is happy; if we detect cycle, it's not happy
• Helper function extracts digits and computes sum of their squares
• Floyd's cycle detection could be used for O(1) space optimization
• Time: O(log n), Space: O(log n)
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False

    def sumOfSquares(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output
        