# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getDepth(node, depth):
            if not node:
                return 0
            curL, curR = 0, 0
            if node.left:
                curL = 1 + getDepth(node.left, depth)
            if node.right:
                curR = 1 + getDepth(node.right, depth)
            depth = max(depth, curL, curR)
            return depth

        return getDepth(root, 1)
        