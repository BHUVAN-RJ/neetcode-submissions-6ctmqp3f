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
        tmpHead = head
        while tmpHead:
            tmp = Node(tmpHead.val)
            nodes[tmpHead] = tmp
            tmpHead = tmpHead.next

        
        for orig, cpy in nodes.items():
            cpy.next = nodes[orig.next] if orig.next in nodes else None
            cpy.random = nodes[orig.random] if orig.random in nodes else None
        
        return nodes[head] if head in nodes else None
        