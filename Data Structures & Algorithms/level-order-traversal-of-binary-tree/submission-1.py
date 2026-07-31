# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        res = [[root.val]]
        q = [(root,0)]
        nextlevel = []

        while q:
            node, level = q.pop(0)
            if node.left:
                q.append((node.left,1+level))
                nextlevel.append(node.left.val)
            if node.right:
                q.append((node.right,1+level))
                nextlevel.append(node.right.val)
            
            if q and q[0][1] != level:
                res.append(nextlevel)
                nextlevel = []

        return res
