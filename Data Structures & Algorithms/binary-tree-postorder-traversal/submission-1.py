# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# stack = [1, 2,]
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root, False)]
        res = []

        while stack:
            cur, v = stack.pop()
            if cur:
                if v:
                    res.append(cur.val)
                else:
                    stack.append((cur, True))
                    stack.append((cur.right, False))
                    stack.append((cur.left, False))
                    
        
        return res
            
        