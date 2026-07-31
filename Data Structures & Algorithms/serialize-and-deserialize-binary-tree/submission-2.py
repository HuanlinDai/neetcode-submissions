# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return 'N'
        nodes = [str(root.val)]
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if node.left:
                nodes.append(str(node.left.val))
                q.append(node.left)
            else:
                nodes.append("N")
            if node.right:
                nodes.append(str(node.right.val))
                q.append(node.right)
            else:
                nodes.append("N")
        return ",".join(nodes)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data[0] == "N":
            return None
        nodes = data.split(",")
        i = 1
        root = TreeNode(int(nodes[0]))
        q = collections.deque([root])
        while i < len(nodes) and q:
            node = q.popleft()
            if nodes[i] != "N":
                node.left = TreeNode(int(nodes[i]))
                q.append(node.left)
            i += 1
            if nodes[i] != "N":
                node.right = TreeNode(int(nodes[i]))
                q.append(node.right)
            i += 1
        return root

