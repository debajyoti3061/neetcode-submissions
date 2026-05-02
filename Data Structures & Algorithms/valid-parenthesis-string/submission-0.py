"""
REVISION NOTES - Valid Parenthesis String:
• Track range of possible open parentheses count using leftMin and leftMax
• '(' increases both min and max by 1
• ')' decreases both min and max by 1
• '*' can be '(', ')' or empty: decrease min by 1, increase max by 1
• If leftMax < 0: too many ')' characters, impossible to balance
• Reset leftMin to 0 if it goes negative (can use '*' as empty)
• Valid if leftMin == 0 at end (can balance all parentheses)
• Time: O(n), Space: O(1)
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0,0
        for i in range(len(s)):
            if s[i] == '(':
                leftMin += 1
                leftMax += 1
            elif s[i] == ')':
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1
            if leftMax < 0:
                return False
            if leftMin < 0 :
                leftMin = 0
        return leftMin == 0
