# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        elements = []
        temp = head
        while temp:
            elements.append(temp)
            temp = temp.next


        size= len(elements)
        left_index = size-k
        k = k-1

        elements[k].val,elements[left_index].val = elements[left_index].val,elements[k].val
   
        return head
