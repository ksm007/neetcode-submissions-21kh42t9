"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        oldList = {None:None}

        curr = head
        while curr:
            copy = Node(curr.val)
            oldList[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = oldList[curr]
            copy.next = oldList[curr.next]
            copy.random = oldList[curr.random]
            curr = curr.next
        
        return oldList[head]