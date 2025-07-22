class Solution:
 

    def get_min(self, root):
        if root is None:
            return None  # or raise an error / return float('inf') if that suits your case
        while root.left:
            root = root.left
        
        return root
    

            

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left,key)
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            print(root.val)
            curr = self.get_min(root.right)
   
            root.val = curr.val
       
            root.right = self.deleteNode(root.right,curr.val)

        return root
            # i have written this solution after watching and understanding neetcode solution. thanks to neetcode for providing best explanations 
