"""
REVISION NOTES - Simplify Path:
• Use stack to track valid directory names in canonical path
• Parse path character by character, building current directory name
• On encountering "/": process current directory name
• ".." means go back (pop from stack if not empty)
• "." and empty strings are ignored
• Valid directory names are pushed to stack
• Join stack elements with "/" to form canonical path
• Time: O(n), Space: O(n)
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""
        for c in path + "/":
            if c == "/":
                if cur == "..":
                    if stack:
                        stack.pop()
                elif cur != "" and cur != ".":
                    stack.append(cur)
                cur = ""
            
            else:
                cur += c
        return "/" + "/".join(stack)


        