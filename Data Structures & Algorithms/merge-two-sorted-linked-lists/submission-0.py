"""
REVISION NOTES - Merge Two Sorted Linked Lists:
• Use dummy node to simplify edge cases
• Compare values of both list heads, attach smaller one
• Move pointer of chosen list forward
• Attach remaining list when one becomes null
• Time: O(n+m), Space: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        
        node.next = list1 or list2
    
        return dummy.next