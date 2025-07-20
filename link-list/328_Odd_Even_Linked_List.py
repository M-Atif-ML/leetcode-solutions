class Solution(object):
    def size_of(self,head):
        size = 0
        while head:
            size+=1
            head = head.next
        return size

    def oddEvenList(self, head):
        if not head:
            return head
        last_element = head
        
        jumps = self.size_of(head)-1
        iterations = 0
        if jumps % 2 ==0:
            iterations = jumps/2
        else:
            iterations = (jumps/2)+1

        while last_element.next:
            last_element =last_element.next
        
        temp = head
        # odd
        for i in range(iterations):
            last_element.next = temp.next
            temp.next= temp.next.next
            last_element = last_element.next
            last_element.next = None
            temp =temp.next
        
        return head
