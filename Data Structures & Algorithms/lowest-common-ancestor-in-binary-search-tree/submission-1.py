# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # returns the path from root to node val
        # assumes val is always present in the BST
        def path(root: TreeNode, val: int) -> List[TreeNode]:
            if root.val == val:
                return [root]
            elif val < root.val:
                temp = path(root.left, val)
                temp.insert(0, root)
                return temp
            else:
                temp = path(root.right, val)
                temp.insert(0, root)
                return temp
        
        p_path = path(root, p.val)
        q_path = path(root, q.val)

        # find the first index where the paths differ
        for i in range(min(len(p_path), len(q_path))):
            if p_path[i].val != q_path[i].val:
                return p_path[i - 1]
        
        # shorter path exhausted, return the last one
        return p_path[-1] if len(p_path) < len(q_path) else q_path[-1]


        