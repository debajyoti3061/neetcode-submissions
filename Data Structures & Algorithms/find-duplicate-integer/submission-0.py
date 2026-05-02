"""
REVISION NOTES - Find Duplicate Integer:
- Use Floyd's cycle detection algorithm
- Treat array as linked list where nums[i] points to nums[nums[i]]
- Find intersection point, then find start of cycle
- Duplicate number is the start of the cycle
- Time: O(n), Space: O(1)
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: 
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2: return slow
        