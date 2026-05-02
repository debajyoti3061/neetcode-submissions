"""
REVISION NOTES - Top K Elements in List:
• Min heap approach to find k most frequent elements
• Count frequency of each element first
• Use min heap of size k to track top k frequent elements
• Push (frequency, element) pairs; pop when heap size > k
• Min heap keeps least frequent at top, so we maintain k most frequent
• Extract elements from heap to get result (order may vary)
• Time: O(n log k), Space: O(n + k)
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1

        heap = []

        for num in count.keys():
            heapq.heappush(heap,(count[num],num))
            if len(heap) > k :
                heapq.heappop(heap)
        res = []
        for i in range(k) :
            res.append(heapq.heappop(heap)[1])
        return res