class Solution(object):

    def modifiedList(self, nums, head):
        hset = {}

        temp = head
        res = ListNode(0)
        while head:
            hset[head.val] =1+ hset.setdefault(head.val,0)
            head =head.next
        print(hset)

        for i in nums:
            if i in hset:
                del hset[i]
        curr = res
        while temp:
            if temp.val in hset:
                curr.next = ListNode(temp.val)
                curr = curr.next
            temp =temp.next

        return res.next
