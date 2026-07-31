# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        

        queue = [(p,q)]
        while queue:
            nodep, nodeq = queue.pop()
            if not nodep and nodeq or not nodeq and nodep:
                return False
            elif not nodep and not nodeq:
                continue
            if nodep.val != nodeq.val:
                return False
            queue.append((nodep.left, nodeq.left))
            queue.append((nodep.right, nodeq.right))

        return True