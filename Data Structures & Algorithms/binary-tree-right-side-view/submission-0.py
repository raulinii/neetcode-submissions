# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # maybe bfs
        # root will always have view
        # do level order where we count len of level
        # if level is greater than or equal to 2 
        # append the last node because its rightmost
        # if level is len 1, return node in that level
        if not root:
            return []
        queue = deque([root])
        result = []

        while queue:
            qLen = len(queue)
            for i in range(qLen):
                curr = queue.popleft()
                if qLen == i+1:
                    result.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return result







