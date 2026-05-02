"""
REVISION NOTES - Find Minimum In Rotated Sorted Array:
- Use binary search to find rotation point
- Compare mid with right element to determine which half is sorted
- Minimum is either at mid or in unsorted half
- Handle edge cases where array is not rotated
- Time: O(log n), Space: O(1)
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            mid = (l+r)//2
            res = min(nums[mid],res)
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return res
        