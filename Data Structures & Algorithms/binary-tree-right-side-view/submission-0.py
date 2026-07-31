# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        res = []
        q = [(root,0)]
        while q:
            node,level = q.pop(0)
            
            if node.left:
                q.append((node.left, 1 + level))
            if node.right:
                q.append((node.right, 1+level))

            if q and q[0][1] != level or not q:
                res.append(node.val)

        return res