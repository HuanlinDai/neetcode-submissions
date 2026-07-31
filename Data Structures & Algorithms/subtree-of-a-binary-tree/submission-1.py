# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root and subRoot or not subRoot and root:
            return False
        elif not root and not subRoot:
            return True

        def isSame(p,q):
            if not p and q or not q and p:
                return False
            elif not q and not p:
                return True
            elif p.val != q.val:
                return False
            return isSame(p.left, q.left) and isSame(p.right, q.right)

        q = [root]

        while q:
            node = q.pop()
            if isSame(node,subRoot):
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return False

        


        