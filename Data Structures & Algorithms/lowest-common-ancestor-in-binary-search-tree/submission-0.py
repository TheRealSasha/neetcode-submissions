# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def path(root, val) -> List[TreeNode]:
            if root.val == val:
                return [root]
            elif val < root.val:
                return [root] + path(root.left, val)
            else:
                return [root] + path(root.right, val)
        
        p_path = path(root, p.val)
        q_path = path(root, q.val)

        for i in range(min(len(p_path), len(q_path))):
            if p_path[i].val != q_path[i].val:
                return p_path[i - 1]
        
        return p_path[-1] if len(p_path) < len(q_path) else q_path[-1]


        