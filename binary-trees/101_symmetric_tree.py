class Solution:
    def check(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False

        return self.check(left.left, right.right) and self.check(left.right,right.left)


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False
        
        return self.check(root.left,root.right)
