"""
REVISION NOTES - Pow(x, n):
• Simple iterative approach: multiply x by itself n times
• Handle edge cases: x=0 returns 0, n=0 returns 1
• For negative exponents, compute positive power then take reciprocal
• Note: This is O(n) solution, can be optimized to O(log n) using fast exponentiation
• Fast exponentiation uses divide-and-conquer: x^n = (x^(n/2))^2
• Time: O(n), Space: O(1)
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        res = 1
        for i in range(abs(n)):
            res *= x
        return res if n >= 0 else 1 / res
        