"""
REVISION NOTES - Duplicate Integer:
- Use set to track seen numbers
- Return true immediately when duplicate found
- Alternative: sort array and check adjacent elements
- Time: O(n), Space: O(n) for set approach
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set1 = set()
        for num in nums:
            if num in set1:
                return True
            set1.add(num)
        return False
        