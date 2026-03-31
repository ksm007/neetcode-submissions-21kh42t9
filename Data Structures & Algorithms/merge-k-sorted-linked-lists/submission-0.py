# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def mergeTwoLists(l1,l2):
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val > l2.val:
                    tail.next = l2
                    l2 = l2.next
                else:
                    tail.next = l1
                    l1 = l1.next
                tail = tail.next
            tail.next = l1 if l1 else l2
            return dummy.next
        res = None
        for l in lists:
            res = mergeTwoLists(res,l)
        return res
            

