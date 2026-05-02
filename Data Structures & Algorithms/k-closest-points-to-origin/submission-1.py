"""
REVISION NOTES - K Closest Points To Origin:
• Calculate squared distance for each point (avoid sqrt for efficiency)
• Use min-heap to store [distance, x, y] for all points
• Heapify the list to create min-heap structure
• Pop k smallest elements from heap to get k closest points
• Return coordinates without distance values
• Time: O(n log n), Space: O(n)
"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []

        for x,y in points:
            dist = x**2 + y**2
            minHeap.append([dist,x,y])
        heapq.heapify(minHeap)
        while k > 0:
            dist,x,y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1
        return res


        