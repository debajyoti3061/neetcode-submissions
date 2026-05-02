"""
REVISION NOTES - Sort Colors:
• Counting sort approach for 3 colors (0, 1, 2)
• Count frequency of each color in first pass
• Reconstruct array by placing colors in order based on counts
• Alternative: Dutch National Flag algorithm with 3 pointers for O(1) space
• This solution uses O(1) extra space for counting array
• Time: O(n), Space: O(1)
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for num in nums:
            count[num] += 1
        index = 0
        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[index] = i
                index += 1
                
