# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        def helper(node, result):
            if not node:
                return

            result.append(node.val)
            helper(node.left, result)
            helper(node.right, result)
        helper(root, result)
        return result