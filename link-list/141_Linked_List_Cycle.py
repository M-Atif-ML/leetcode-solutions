# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head is None or head.next is None:
            return False
        sset = set()

        temp  =head

        while temp:
            sset.add(temp)
            if temp.next in sset:
                return True
            temp =temp.next
        return False

        
