"""
REVISION NOTES - Longest Consecutive Sequence:
• Use set for O(1) lookup of numbers
• Only start counting from numbers that are beginning of sequences (num-1 not in set)
• For each sequence start, count consecutive numbers by incrementing
• Track maximum sequence length found
• This avoids counting same sequence multiple times
• Time: O(n), Space: O(n)
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxlen = 0
        for num in numSet:
            if (num-1) not in numSet :
                length = 1
                while (num+length) in numSet :
                    length += 1
                maxlen = max(maxlen, length)
        return maxlen
        