"""
REVISION NOTES - Remove Duplicates From Sorted Array:
• Two-pointer approach: left pointer for unique elements, right pointer for scanning
• Place unique elements at left pointer position
• Skip all duplicates by advancing right pointer while values are same
• Return left pointer as length of unique elements
• Modifies array in-place to save space
• Time: O(n), Space: O(1)
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l = r = 0
        while r < n :
            nums[l] = nums[r]
            while r < n and nums[l] == nums[r] :
                r += 1
            l += 1
        return l
        