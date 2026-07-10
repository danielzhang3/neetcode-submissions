# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, prevMax): 
            nonlocal res
            if not node: 
                return 0
            if node.val >= prevMax: 
                res += 1
            prevMax = max(node.val, prevMax)
            dfs(node.left, prevMax)
            dfs(node.right, prevMax)
        
        dfs(root, float("-inf"))
        return res
        