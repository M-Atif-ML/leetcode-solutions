class Solution:
    def get_size(self, head):
        size = 0
        while head:
            head = head.next
            size += 1
        return size

    def rotateRight(self, head, k):
        size = self.get_size(head)
        if size == 0 or size == 1:
            return head

        k = k % size
        if k == 0:
            return head


        ind = 0
        liter = head
        new_head = None
        while liter:
            if ind == size - k - 1:
                new_head = liter.next
                liter.next = None
                break
            ind += 1
            liter = liter.next
        # print(temp.val)
        temp =  new_head
        while True:
            if new_head.next == None:
                new_head.next = head
                head= new_head
                break
            new_head = new_head.next
        
        return temp
        
        
        
