"""
REVISION NOTES - Find Target In Rotated Sorted Array:
- First determine which half of array is properly sorted
- Check if target lies in sorted half, otherwise search other half
- Use standard binary search logic within sorted portions
- Handle rotation by comparing mid with left/right boundaries
- Time: O(log n), Space: O(1)
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid -1
                else:
                    l = mid + 1
        return -1
        