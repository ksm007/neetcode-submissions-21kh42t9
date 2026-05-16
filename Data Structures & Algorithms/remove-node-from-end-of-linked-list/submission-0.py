# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s = 0
        curr = head
        while curr:
            s+=1
            curr = curr.next
        curr = head
        t = s-n
        if t == 0:
            return head.next
        s = 0
        while curr:
            s+=1
            if s == t:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head
