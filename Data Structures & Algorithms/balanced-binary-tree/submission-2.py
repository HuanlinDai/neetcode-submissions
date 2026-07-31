# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        
        def dfs(node):
            if not node:
                return (True, 0)

            lbal, lh = dfs(node.left)
            rbal, rh = dfs(node.right)
            if not lbal or not rbal or abs(lh-rh) > 1:
                return (False,-1)
            return (True, 1 + max(lh, rh))

        return dfs(root)[0]