"""
REVISION NOTES - Asteroid Collision:
• Use stack to simulate asteroid movements
• Positive asteroids (moving right) go on stack
• Negative asteroids (moving left) may collide with stack top
• Handle collision cases: destruction, survival, mutual destruction
• Time: O(n), Space: O(n)
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for num in asteroids:
            if num > 0 :
                stack.append(num)
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(num):
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(num)
                if stack[-1] == abs(num):
                    stack.pop()
        return stack
        