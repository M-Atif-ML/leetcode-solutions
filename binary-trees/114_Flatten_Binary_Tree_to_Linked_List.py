class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root or not root.left and not root.right:
            return 

        temp = root
        stack = [temp]
        temp_list = []
        while stack and temp:
            temp = stack.pop()
            temp_list.append(temp)

            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)


        for i in range(len(temp_list)-1):
            temp_list[i].right = temp_list[i+1]
            temp_list[i].left = None

            
      
       
        root =  temp_list[0]
