# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
curmax - 2 
 2 -> good
 1 -> bad
 3 -> curmax -> 3 -> good
 other side

 curmax = 1
 1 -> good
 -1 -> bad
 2 -> curmax = 2 -> good
 3 -> curmax = 3 -> good !!!!!!! 4 -> curmax = 4 -> good


'''
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        curmax = None
        count = 0

        def dfs(node, curmax):
            nonlocal count
            if not node:
                return 
            
            if curmax is None:
                curmax = node.val
                count += 1
            elif node.val >= curmax:
                count += 1
            
            curmax = max(node.val, curmax)
            
            dfs(node.left, curmax)
            dfs(node.right, curmax)

            return
        
        dfs(root, curmax)
        return count

        