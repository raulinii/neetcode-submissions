# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # global list 
        # dfs with two variables, (node, curr max)
        # curr max is 1
        # run on left with max 
        # run on right with max
        # -----
        # track the root value somehow, maybe global?
        # we need to compare the root, max on the current path
        # and the node value were currently at
            def dfs(root, maxVal):
                if not root:
                    return 0
                if root.val >= maxVal:
                    res = 1
                else:
                    res = 0
                maxVal = max(root.val, maxVal)
                res += dfs(root.left,maxVal)
                res += dfs(root.right,maxVal)
                return res
            return dfs(root,root.val)
                





