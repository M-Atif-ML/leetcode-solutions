class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root and val:
            root = TreeNode(val,None,None)
            return root 
        if val > root.val:
            if root.right:
                root.right = self.insertIntoBST(root.right,val)
            else:
                root.right= TreeNode(val,None,None)
        elif val<root.val:
            if root.left:
               root.left =  self.insertIntoBST(root.left,val)
            else:
                root.left = TreeNode(val,None,None)
        return root
