"""
REVISION NOTES - Implement Queue Using Stacks:
• Use two stacks: s1 for input, s2 for output
• Push: Always add to s1
• Pop/Peek: If s2 is empty, transfer all elements from s1 to s2, then pop/peek from s2
• This ensures FIFO order (first in, first out) using LIFO stacks
• Amortized O(1) for all operations
• Time: O(1) amortized, Space: O(n)
"""

class MyQueue:

    def __init__(self):
        self.s1= []
        self.s2 = []
        

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            while (self.s1):
                self.s2.append(self.s1.pop())

        return self.s2.pop()
        

    def peek(self) -> int:
        if not self.s2:
            while (self.s1):
                self.s2.append(self.s1.pop())

        return self.s2[-1]
        

    def empty(self) -> bool:
        return max(len(self.s1), len(self.s2)) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()