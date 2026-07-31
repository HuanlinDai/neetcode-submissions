# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        self.inorderinds = {val: ind for ind, val in enumerate(inorder)}
        def dfs(preorder, left, right):
            if not preorder:
                return None
            val = preorder[0]
            ind = self.inorderinds[val]
            if ind < left or ind > right:
                return None
            
            node = TreeNode(preorder.pop(0))
            node.left = dfs(preorder, left, ind-1)
            node.right = dfs(preorder, ind+1, right)

            return node

        return dfs(preorder, 0, len(preorder)-1)