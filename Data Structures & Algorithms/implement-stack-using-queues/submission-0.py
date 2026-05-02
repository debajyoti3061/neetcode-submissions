"""
REVISION NOTES - Implement Stack Using Queues:
• Use single queue (deque) to simulate stack behavior
• Push: Simply append to queue
• Pop: Rotate queue n-1 times to bring last element to front, then pop
• Top: Access last element directly (queue[-1])
• Empty: Check if queue length is 0
• Time: Push O(1), Pop O(n), Top O(1), Empty O(1), Space: O(n)
"""

class MyStack:

    def __init__(self):
        self.q = deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        for i in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        return self.q.popleft()
        

    def top(self) -> int:
        return self.q[-1]
        

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()