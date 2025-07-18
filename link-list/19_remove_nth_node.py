class Solution(object):
    def size_of(self,head):
        s = 0
        lst=head
        while lst:
            lst = lst.next
            s+=1
        return s

    def removeNthFromEnd(self, head, n):
        if self.size_of(head) == 1 and n is not None:
            return None

        n = self.size_of(head)-n
        if n == 0:
            return head.next
        iter = 0
        lst = head
        while lst:
            iter +=1
            if iter == n and lst.next != None:
                lst.next = lst.next.next
                break
            lst = lst.next
        return head
