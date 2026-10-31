# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # we need child data
        # go down tree
        # get left child
        # get right child
        # compare with parent
        # maybe a dfs that returns val of curr node and state(T/F)
        def dfs(node, left, right):
            if not node:
                return True
            
            if not (left < node.val < right):
                return False
            
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
        return dfs(root, float("-inf"), float("+inf"))
            
            







