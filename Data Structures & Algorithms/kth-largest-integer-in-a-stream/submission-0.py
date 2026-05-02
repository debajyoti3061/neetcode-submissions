"""
REVISION NOTES - Kth Largest Integer In A Stream:
• Use min-heap of size k to maintain k largest elements
• Initialize: heapify array, then remove excess elements to keep only k largest
• Add operation: push new value, then pop if heap size exceeds k
• Root of min-heap (arr[0]) is always the kth largest element
• Min-heap ensures smallest of k largest is at root
• Time: Init O(n log n), Add O(log k), Space: O(k)
"""

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr, self.k = nums, k
        heapq.heapify(self.arr)
        while len(self.arr) > k:
            heapq.heappop(self.arr)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.arr,val)
        if len(self.arr) > self.k:
            heapq.heappop(self.arr)
        return self.arr[0]
        
