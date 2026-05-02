"""
REVISION NOTES - Search Insert Position:
• Binary search to find target or insertion position
• If target found, return its index
• If target not found, left pointer will be at correct insertion position
• Left pointer naturally moves to where target should be inserted
• Works because binary search maintains sorted order invariant
• Time: O(log n), Space: O(1)
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0 , len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid-1
        return l
        