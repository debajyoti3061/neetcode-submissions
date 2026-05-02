"""
REVISION NOTES - Roman To Integer:
• Use hashmap to store roman numeral values
• Iterate through string, check if current character should be subtracted
• If current value < next value, subtract (handles IV, IX, XL, XC, CD, CM cases)
• Otherwise, add the value normally
• This handles subtractive notation automatically
• Time: O(n), Space: O(1)
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500, "M": 1000
        }
        res = 0
        for i in range(len(s)):
            if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res