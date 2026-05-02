"""
REVISION NOTES - Binary Search:
• Use two pointers (left, right) to define search space
• Calculate mid point, compare with target
• Adjust search space based on comparison
• Continue until target found or search space exhausted
• Time: O(log n), Space: O(1)
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i , j = 0, len(nums)-1
        while i <= j:
            mid = (i+j)//2
            if target > nums[mid]:
                i = mid+1
            elif target < nums[mid]:
                j = mid-1
            elif target == nums[mid]:
                return mid
        return -1
        