# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr2 = slow.next
        slow.next = None
        prev = None
        while curr2:
            tmp = curr2.next
            curr2.next = prev
            prev = curr2
            curr2 = tmp
        # merge 2 halves of the list
        second = prev
        first = head
        while second:
            tmp1,tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1,tmp2