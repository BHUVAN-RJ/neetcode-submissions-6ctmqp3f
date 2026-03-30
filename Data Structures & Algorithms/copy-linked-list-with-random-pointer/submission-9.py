"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}
        if not head: return None
        copyHead = head
        while copyHead:
            nodes[copyHead] = Node(copyHead.val)
            copyHead = copyHead.next

        for node, copyNode in nodes.items():
            if node.next:
                copyNode.next = nodes[node.next]
            if node.random:
                copyNode.random = nodes[node.random]
        
        return nodes[head]

        
