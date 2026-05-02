"""
REVISION NOTES - Reverse String:
• Two-pointer approach: swap characters from both ends moving inward
• Use left and right pointers starting at opposite ends
• Swap characters at these positions and move pointers toward center
• Continue until pointers meet in the middle
• Modifies array in-place as required
• Time: O(n), Space: O(1)
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        i = 0
        j = len(s) - 1
        while i < j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1
        return s 
        