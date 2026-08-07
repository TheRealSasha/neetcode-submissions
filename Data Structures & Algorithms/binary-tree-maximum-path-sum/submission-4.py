# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # node -> (left, right)
        dp = dict()

        def helper(root):
            if not root:
                return -math.inf

            if root in dp:
                return dp[root][0]
            
            left = helper(root.left)
            right = helper(root.right)
            
            dp[root] = (root.val + max(0, left, right), root.val + max(0, right) + max(0, left))

            return dp[root][0]
        
        helper(root)

        return max(item for t in dp.values() for item in t)



        