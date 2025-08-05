class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        q = deque()
        q.appendleft(root)
        temp = root

        while q:
            tempNodes = []
            for i in range(len(q)):
                temp = q.pop()

                tempNodes.append(temp)

                if temp.left:
                    q.appendleft(temp.left)
                if temp.right:
                    q.appendleft(temp.right)
            for i in range(0,len(tempNodes)+1):
                if i+1 < len(tempNodes):
                    tempNodes[i].next = tempNodes[i+1]
  
        return root

# not the best solution but its 100% written by me no youtube and no gpt 
# Time : O(n+m) because we are visiting each node 2 times separately
# Space : O(n)
