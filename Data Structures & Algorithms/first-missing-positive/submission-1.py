"""
REVISION NOTES - First Missing Positive:
• Use boolean array of size n to track presence of numbers 1 to n
• Only consider positive numbers within range [1, n]
• Mark corresponding index as True for each valid number
• Find first False position to get missing positive number
• If all positions are True, return n+1
• Time: O(n), Space: O(n)
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = [False] * len(nums)
        for num in nums:
            if num > 0 and num <= len(nums):
                seen[num-1] = True
        for i in range(1,len(seen)+1):
            if not seen[i-1]:
                return i
        return len(nums)+1

        