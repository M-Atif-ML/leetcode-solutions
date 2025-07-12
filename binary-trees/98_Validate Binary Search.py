# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        nums = []

        def inOrder(root):
            if not root:
                return

            inOrder(root.left)
            nums.append(root.val)
            inOrder(root.right)
        inOrder(root)
        print(nums)
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                return False
        return True
