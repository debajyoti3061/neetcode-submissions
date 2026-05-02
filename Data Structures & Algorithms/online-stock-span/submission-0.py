"""
REVISION NOTES - Online Stock Span:
• Use monotonic decreasing stack to track (price, span) pairs
• For each new price, pop all smaller/equal prices and accumulate their spans
• Stack maintains prices in decreasing order from bottom to top
• Current span = 1 + sum of spans of all popped elements
• Push current (price, span) to stack for future calculations
• Time: O(1) amortized, Space: O(n)
"""

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price,span))
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)