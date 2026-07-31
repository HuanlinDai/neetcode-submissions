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
        res = []

        q = [(root, 0)]
        curlevel = []
        while q:
            node, level = q.pop(0)
            curlevel.append(node.val)
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
            if q and level != q[0][1]:
                res.append(curlevel)
                curlevel = []
        res.append(curlevel)
        return res