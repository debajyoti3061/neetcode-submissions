"""
REVISION NOTES - Decode String:
- Use stack to handle nested brackets
- Push characters until ']' encountered
- When ']' found, pop string and number, repeat and push back
- Handle multi-digit numbers correctly
- Time: O(n), Space: O(n)
"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                res = ""
                while stack and stack[-1] != "[":
                    res = stack.pop() + res
                stack.pop()
                count = ""
                while stack and stack[-1].isdigit():
                    count = stack.pop() + count
                
                stack.append(int(count) * res)

        return "".join(stack)



        