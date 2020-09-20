# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res =[]
        def help(root):
            if not root:
                return
            help(root.left)
            res.append(root.val)
            help(root.right)
        help(root)
        return res