# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        res = self.traverse(root, 1, res)
        return res
        
    def traverse(self, node, level, res):
        if not node:
            return res
        if len(res) < level:
            res.append([])
        
        res[level - 1].append(node.val)
        res = self.traverse(node.left, level+1, res)
        res = self.traverse(node.right, level+1, res)

        return res
        
        