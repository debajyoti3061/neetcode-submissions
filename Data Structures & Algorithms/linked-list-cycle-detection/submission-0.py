"""
REVISION NOTES - Linked List Cycle Detection:
- Use Floyd's cycle detection (tortoise and hare)
- Slow pointer moves one step, fast pointer moves two steps
- If cycle exists, fast will eventually meet slow
- If fast reaches null, no cycle exists
- Time: O(n), Space: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        