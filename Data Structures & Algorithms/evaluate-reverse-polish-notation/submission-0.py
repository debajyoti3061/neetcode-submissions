"""
REVISION NOTES - Evaluate Reverse Polish Notation:
- Use stack to store operands
- For numbers, push onto stack
- For operators, pop two operands, compute result, push back
- Handle division carefully for negative numbers
- Time: O(n), Space: O(n)
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop()+ stack.pop())
            elif c == "*" :
                stack.append(stack.pop()*stack.pop())
            elif c == "-":
                a,b = stack.pop() , stack.pop()
                stack.append(b-a)
            elif c == "/":
                a,b = stack.pop() , stack.pop()
                stack.append(int(float(b)/a))
            else:
                stack.append(int(c))
        return stack[0]
        


        