# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        elif not root:
            return False

        q = [root]
        while q:
            node = q.pop(0)
            if self.sameTree(node, subRoot):
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False
            

    def sameTree (self, ptree: Optional[TreeNode], qtree: Optional[TreeNode]) -> bool:
        if not ptree and not qtree:
            return True
        elif not ptree or not qtree:
            return False

        if ptree.val != qtree.val:
            return False
        
        return self.sameTree(ptree.left, qtree.left) and self.sameTree(ptree.right, qtree.right)