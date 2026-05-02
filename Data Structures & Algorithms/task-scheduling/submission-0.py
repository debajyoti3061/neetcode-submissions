"""
REVISION NOTES - Task Scheduling:
• Max heap + queue approach to handle cooldown periods
• Use max heap to always process most frequent task first
• Queue stores tasks in cooldown with their available time
• At each time unit: process from heap, add to queue if remaining count > 0
• Check queue for tasks ready to return to heap (cooldown expired)
• Continue until both heap and queue are empty
• Time: O(n log k) where k is unique tasks, Space: O(k)
"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt,time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time
                