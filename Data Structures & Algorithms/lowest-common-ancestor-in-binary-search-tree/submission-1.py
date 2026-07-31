# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pfound = None
        qfound = None

        queue = [(root, [root.val])]

        while queue and (not pfound or not qfound):
            node, trace = queue.pop(0)
            if node.val == p.val:
                pfound = trace
            if node.val == q.val:
                qfound = trace
            if node.left:
                queue.append((node.left, trace + [node.left.val]))
            if node.right:
                queue.append((node.right, trace + [node.right.val]))
        print(pfound, qfound)
        last_known_ancestor = None
        last_known_ind = None
        for i in range(min(len(pfound), len(qfound))):
            if pfound[i] != qfound[i]:
                break
            else:
                last_known_ancestor = pfound[i]
                last_known_ind = i

        trace = pfound[:last_known_ind+1]
        print(trace)

        cur = root
        for i in range(len(trace) - 1):
            if cur.left and cur.left.val == trace[i+1]:
                cur = cur.left
            elif cur.right and cur.right.val == trace[i+1]:
                cur = cur.right
        return cur
