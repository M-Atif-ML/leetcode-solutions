    def kthSmallest(self, root, k):
        nums = []
        q = deque()
        q.appendleft(root)
        while q:
            root = q.pop()
            nums.append(root.val)
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
        
        heapq.heapify(nums)
        mmin  = 0
        print(nums)
        for i in range(k+1):
            if i == k:
                break
            mmin = heapq.heappop(nums)
        return mmin
# here i have used a different method thats not really effecient but i have done this to practice heaps
