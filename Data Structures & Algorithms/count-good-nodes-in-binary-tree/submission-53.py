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
                return
            if node.val >= prevMax: 
                res += 1
            prevMax = max(prevMax, node.val)
            dfs(node.left, prevMax)
            dfs(node.right, prevMax)
        
        dfs(root, float("-inf"))
        return res
        