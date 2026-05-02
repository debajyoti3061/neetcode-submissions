"""
REVISION NOTES - Sliding Window Maximum:
- Use deque to maintain indices of potential maximum elements
- Remove indices outside current window from front
- Remove smaller elements from back before adding new element
- Front of deque always contains index of maximum in current window
- Time: O(n), Space: O(k)
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []
        for i in range (len(nums)):
            heapq.heappush(heap,(-nums[i],i))

            if i >= k-1:
                while heap[0][1] <= i-k :
                    heapq.heappop(heap)
                output.append(-heap[0][0])
        return output

        