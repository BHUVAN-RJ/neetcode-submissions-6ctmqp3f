# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'meaning node x should be the greatest val from the root including the root'
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def preOrder(node, maxVal):
            if not node:
                return 0
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += preOrder(node.left, maxVal)
            res += preOrder(node.right, maxVal)
            return res
        
        return preOrder(root, root.val)


        