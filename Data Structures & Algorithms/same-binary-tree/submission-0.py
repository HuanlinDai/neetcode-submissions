# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True
        elif not p or not q:
            return False

        pqueue = [p]
        qqueue = [q]

        while pqueue and qqueue:
            pnode = pqueue.pop(0)
            qnode = qqueue.pop(0)

            if (not pnode.left and qnode.left) or (pnode.left and not qnode.left) or (pnode.right and not qnode.right) or (not pnode.right and qnode.right) or pnode.val != qnode.val:
                return False

            if pnode.left and qnode.left:
                pqueue.append(pnode.left)
                qqueue.append(qnode.left)
            if pnode.right and qnode.right:
                pqueue.append(pnode.right)
                qqueue.append(qnode.right)

        return True