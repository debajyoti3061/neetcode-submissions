"""
REVISION NOTES - Plus One:
• Simulate addition from rightmost digit (least significant)
• If digit < 9, increment and return (no carry needed)
• If digit = 9, set to 0 and continue to next digit (carry over)
• If all digits are 9, prepend 1 to array of zeros
• Process digits from right to left to handle carry properly
• Time: O(n), Space: O(1) or O(n) if new array needed
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
        