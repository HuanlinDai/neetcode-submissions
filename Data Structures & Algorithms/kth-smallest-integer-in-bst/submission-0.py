# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visited = set({})
        stack = [root]
        i = 0
        while stack:
            node = stack[-1]
            if node.left:
                if node.left.val not in visited:
                    stack.append(node.left)
                    continue
            i += 1
            if i == k:
                return node.val
            visited.add(node.val)
            stack.pop(-1)
            if node.right:
                if node.right.val not in visited:
                    stack.append(node.right)
            