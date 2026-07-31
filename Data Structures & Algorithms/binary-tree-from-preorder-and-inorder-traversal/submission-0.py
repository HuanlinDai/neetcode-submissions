# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorderInds = {}
        for i in range(len(inorder)):
            inorderInds[inorder[i]] = i

        def build(preorder, left, right):
            if not preorder:
                return None
            val = preorder[0]
            ind = inorderInds[val]
            if ind < left or ind > right:
                return None
            preorder.pop(0)
            node = TreeNode(val)
            node.left = build(preorder, left, ind - 1)
            node.right = build(preorder, ind + 1, right)
            return node

        return build(preorder, 0, len(preorder)-1)