"""
REVISION NOTES - Majority Element:
• Use hashmap to count frequency of each element
• Track element with maximum count seen so far
• Update result whenever a new maximum count is found
• Majority element appears more than n/2 times, so will have highest count
• Alternative: Boyer-Moore voting algorithm for O(1) space
• Time: O(n), Space: O(n)
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = defaultdict(int)
        maxCount = res = 0
        for num in nums:
            map[num] += 1
            
            if maxCount < map[num] :
                res = num
                maxCount = map[num]
        return res
        