"""
REVISION NOTES - Minimum Stack:
• Use two stacks: main stack for values, minStack for tracking minimums
• Push: add value to main stack, add current minimum to minStack
• Pop: remove from both stacks simultaneously
• getMin: return top of minStack (current minimum)
• Maintains O(1) time for all operations
• Time: O(1) for all operations, Space: O(n)
"""

class MinStack:

    def __init__(self):
        self.s = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.s.append(val)
        val = min (val, self.minStack[-1] if self.minStack  else val)
        self.minStack.append(val)
        

    def pop(self) -> None:
        self.s.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
