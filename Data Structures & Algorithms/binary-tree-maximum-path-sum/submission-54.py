# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        def dfs(node): 
            nonlocal res 
            if not node: 
                return 0
            node.left = max(0, dfs(node.left))
            node.right = max(0, dfs(node.right))
            candidate = node.val + node.left + node.right
            res = max(res, candidate)
            return node.val + max(node.left, node.right)
        
        dfs(root)
        return res
        