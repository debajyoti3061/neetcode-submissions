"""
REVISION NOTES - Last Stone Weight:
• Use max-heap to always get the two heaviest stones
• Python heapq is min-heap, so negate values to simulate max-heap
• Pop two heaviest stones, smash them together
• If weights differ, push the difference back to heap
• Continue until at most one stone remains
• Time: O(n log n), Space: O(n)
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1 :
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones,first-second)
        stones.append(0)
        return -stones[0]

        