"""
REVISION NOTES - Validate Parentheses:
- Use stack to track opening brackets
- Push opening brackets onto stack
- For closing brackets, check if stack top matches
- Stack should be empty at end for valid parentheses
- Time: O(n), Space: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[' :
                stack.append(s[i])
            elif s[i] == ')' :
                if not stack or stack.pop() != '(':
                    return False
            elif s[i] == '}' :
                if not stack or stack.pop() != '{':
                    return False
            elif s[i] == ']' :
                if not stack or stack.pop() != '[':
                    return False
        return len(stack) == 0
        