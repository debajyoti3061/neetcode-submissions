"""
REVISION NOTES - Contains Duplicate Ii:
- Use hashmap to store number and its most recent index
- For each number, check if seen before within k distance
- Update index in hashmap for current number
- Return true if duplicate found within k distance
- Time: O(n), Space: O(n)
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}
        for i in range(len(nums)):
            if nums[i] in map and i-map[nums[i]] <= k :
                return True
            map[nums[i]] = i
        return False
        