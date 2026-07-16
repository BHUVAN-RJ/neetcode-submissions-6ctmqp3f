# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
INorder : left root right
in - head of the tree
out - an array of node values of the tree
goal - traverse the tree inorder and then return the values accordingly

examples: 
1.normal case -> 4, 2, 5, 1, 6, 3, 7
2. cases where we do not have some nodes in the tree -> 2, 4, 1, 5 ,3
3. empty -> empty

some more cases:
4. one node - one node
5. skewed tree - return accordingly 

solution/hypothesis:
we use recursion - cal it on left then root then right
end condition - if no children( leaf node)

global res
if not root:
    return

def traverse :
if not node.left and not node.right:
    res.append(val)
    return
if node.left:
    traverse(node.left, res)
res.append(node.val)
if node.right:
    traverse(node.right, res)
return
dry run:
1. stack = [ ] - res = [4, 2, 5, 6, 3, 7, 1]
2. stack = [1 -> 3 -> 5] - res = [2, 4, 1, 5, 3]
3. done
'''
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        def traverse(node):
            if not node.left and not node.right:
                res.append(node.val)
                return
            
            if node.left:
                traverse(node.left)
            res.append(node.val)
            if node.right:
                traverse(node.right)
            return
        traverse(root)
        return res







