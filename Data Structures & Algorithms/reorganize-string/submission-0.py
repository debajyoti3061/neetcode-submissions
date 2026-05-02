"""
REVISION NOTES - Reorganize String:
• Use max-heap to always pick character with highest frequency
• Avoid placing same character consecutively by using previous character buffer
• Pop most frequent character, add to result, store in prev if count > 0
• Push previous character back to heap before processing next
• If heap is empty but prev exists, reorganization is impossible
• Time: O(n log k), Space: O(k) where k is unique characters
"""

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt,char] for char,cnt in count.items()]
        heapq.heapify(maxHeap)
        prev = None
        res = ""

        while maxHeap or prev:
            if not maxHeap and prev:
                return ""
            cnt, char = heapq.heappop(maxHeap)

            res += char
            cnt += 1
            if prev:
                heapq.heappush(maxHeap,prev)
                prev = None
            if cnt != 0:
                prev = [cnt,char]
        return res


        