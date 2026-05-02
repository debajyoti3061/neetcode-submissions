"""
REVISION NOTES - Two Integer Sum:
• Use hashmap to store target - current_number as key and index as value
• Check if current number exists in hashmap before adding complement
• Return indices when complement is found
• Time: O(n), Space: O(n)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] = i
        
