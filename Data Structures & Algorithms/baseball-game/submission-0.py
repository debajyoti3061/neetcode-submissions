"""
REVISION NOTES - Baseball Game:
- Use stack to track valid scores
- Handle operations: + (sum last two), D (double last), C (cancel last)
- For numbers, convert to int and push to stack
- Return sum of all elements in stack
- Time: O(n), Space: O(n)
"""

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for c in operations:
            if c == "+" :
                stack.append(stack[-1]+stack[-2])
            elif c == "D" :
                stack.append(stack[-1] * 2)
            elif c == "C" :
                stack.pop()
            else :
                stack.append(int(c))
        return sum(stack)

        