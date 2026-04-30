# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        def merge2sorted(l1,l2):
            node = dummy = ListNode()

            while l1 and l2:
                if l1.val <= l2.val:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2= l2.next
                node = node.next
            if l1:
                node.next = l1
            else:
                node.next = l2
            return dummy.next
        
        while len(lists) >1:
            mergedLists = []
            for i in range(0,len(lists),2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(merge2sorted(list1,list2))
            lists = mergedLists
        return lists[0]
            

        

        