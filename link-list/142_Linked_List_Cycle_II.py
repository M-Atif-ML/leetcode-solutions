# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        sset = set()
        hset = {}
        pos = 0
        
        while head:
            sset.add(head)
            if head.next in sset:
                return head.next
            head =head.next
            pos+=1
        return None
