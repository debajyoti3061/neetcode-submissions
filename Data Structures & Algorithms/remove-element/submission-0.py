"""
REVISION NOTES - Remove Element:
• Two-pointer approach: k tracks position for valid elements
• Iterate through array, copy non-target elements to position k
• Only increment k when element is not equal to val
• Return k as the new length of array without target elements
• Modifies array in-place to save space
• Time: O(n), Space: O(1)
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k



        