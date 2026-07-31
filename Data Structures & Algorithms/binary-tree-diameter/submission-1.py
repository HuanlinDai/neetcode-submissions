# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
            

        def dfs(node):
            if not node:
                return 0, 0
            lefth, leftd= dfs(node.left)
            righth, rightd = dfs(node.right)
            bestd = max(leftd, rightd, lefth + righth)
            return 1 + max(lefth,righth), bestd

        h, d = dfs(root)
        return d