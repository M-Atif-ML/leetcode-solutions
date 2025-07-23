class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def dfs(root,num):
            if not root:
                return 
            num =num *10 + root.val
            if not root.left and not root.right:
                res.append(num)
            dfs(root.left,num)
            dfs(root.right,num)
        num = 0
        dfs(root,num)

        # print(res)


        return sum(res)
