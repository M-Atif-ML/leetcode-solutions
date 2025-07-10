# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, node):
        q = deque()

        l = []

        q.appendleft(node)

        while q and node:
            node = q.pop()
            l.append(node.val)
            if node.right == None and node.left:
                node.right = TreeNode(None)
            if node.left == None and node.right:
                node.left = TreeNode(None)

            if node.left:
                q.appendleft(node.left)
            if node.right:
                q.appendleft(node.right)
            
        return l
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        print(self.bfs(p))
        print(self.bfs(q))
        return self.bfs(p) == self.bfs(q)

# time complexity is O(n) and space is also O(n) since we are creating a list of elements depending on number of nodes in tree 
