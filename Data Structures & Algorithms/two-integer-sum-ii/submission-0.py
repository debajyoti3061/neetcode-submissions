"""
REVISION NOTES - Two Integer Sum Ii:
- Use two pointers from start and end of sorted array
- Move left pointer right if sum too small, right pointer left if sum too large
- Return indices when target sum found
- Works because array is sorted
- Time: O(n), Space: O(1)
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = defaultdict(int)
        for i in range(len(numbers)):
            temp = target-numbers[i]
            if temp in map.keys():
                return [map[temp],i+1]
            map[numbers[i]] = i+1
        return []    