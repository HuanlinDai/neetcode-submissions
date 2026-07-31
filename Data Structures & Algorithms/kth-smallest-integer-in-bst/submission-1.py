# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.visited = 0
        def dfs(node):

            if not node:
                return -1 # value, kth node
            
            val = dfs(node.left)
            self.visited += 1
            if self.visited == k:
                return node.val
            elif val != -1:
                return val
            return dfs(node.right)

            
        return dfs(root)