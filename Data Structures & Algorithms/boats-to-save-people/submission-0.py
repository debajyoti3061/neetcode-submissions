"""
REVISION NOTES - Boats To Save People:
- Sort people by weight, use two pointers
- Try to pair lightest and heaviest person in each boat
- If both can fit (weight <= limit), move both pointers
- Otherwise, only take heavier person and move right pointer
- Time: O(n log n), Space: O(1)
"""

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res , l , r = 0 , 0 , len(people)-1
        while l <= r :
            remain = limit - people[r]
            r -= 1
            res += 1
            if l <= r and remain >= people[l] :
                l += 1
        return res

        