# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0

        def dfs(node, maxseen):
            res = 0
            if node.val >= maxseen:
                res += 1
            if node.left:
                res += dfs(node.left, max(maxseen, node.val))
            if node.right:
                res += dfs(node.right, max(maxseen, node.val))
            return res

        return dfs(root,root.val)