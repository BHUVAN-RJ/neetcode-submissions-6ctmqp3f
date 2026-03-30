# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getDiameter(root, diameter):
            if not root: return [0, 0]

            left, right = getDiameter(root.left, diameter), getDiameter(root.right, diameter)
            curDiameter = left[0] + right[0]

            return [1 + max(left[0], right[0]), max(diameter, left[1], right[1], curDiameter)]
        diameter = getDiameter(root, 0)
        return diameter[1]
        