# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
very simple - if the children are diverging then it just means that particular node is the LCA

3 cases:
1. both on same side - then change root = root.left/right and keep going until 
2. on different sides - that node is the answer
3. either p/q is the node - then the node itself is the LCA

'''
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            if node.val == p.val or node.val == q.val or p.val < node.val < q.val or q.val < node.val < p.val:
                return node
            
            elif p.val < node.val and q.val < node.val:
                res = dfs(node.left)
            elif p.val > node.val and q.val > node.val:
                res = dfs(node.right)
            return res
        return dfs(root)
        