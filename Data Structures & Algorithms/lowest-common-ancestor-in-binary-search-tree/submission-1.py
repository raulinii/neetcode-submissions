# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # use root to find which way we need to check for values for
        # example: lca of 3 and 8 is 5
        # we know the general direction of 3 and 8 bc bst
        # 3 < root < 8. This means our values are on the left and right
        # use bst property
        # prop 1: both p and q bigger than root
        # lca of 7 and 9 = 8
        # if if p.val and q.val > root.val check right side
        # prop 2: both p and q smaller than root
        # lca of 1 and 4 = 3
        # prop 3: one smaller than root and one bigger
        # lca of 3 and 8 = 5

        if not root or not p or not q:
            return None
        # go left
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # go right
        if min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
