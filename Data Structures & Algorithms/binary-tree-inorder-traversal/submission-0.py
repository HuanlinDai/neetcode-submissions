# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        self.res = []

        def dfs(node):
            if node is None:
                return
            # first, add values of the left subtree
            dfs(node.left)
            # second, record the value of the node we're at
            self.res.append(node.val)
            # third, add values of the right subtree
            dfs(node.right)
            return

        dfs(root)

        return self.res