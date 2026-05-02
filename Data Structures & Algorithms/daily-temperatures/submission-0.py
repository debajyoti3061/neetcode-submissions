"""
REVISION NOTES - Daily Temperatures:
- Use stack to store indices of temperatures
- For each temperature, pop indices with smaller temperatures
- Calculate days difference for popped indices
- Push current index onto stack
- Time: O(n), Space: O(n)
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI]= i-stackI
            stack.append((t,i))
        return res
        