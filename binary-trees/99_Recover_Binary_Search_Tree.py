class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        ans=  []   
        # temp = root


        def in_order(root):
            if not root:
                return
            
            in_order(root.left)
            ans.append(root)
            in_order(root.right)
        in_order(root)   
        print(ans)
        srt = sorted(i.val for i in ans)
        print(srt)
        for i in range(len(srt)):
            ans[i].val = srt[i]
        
        # i learned this solution from internet after fully unserstanding the solution

        
