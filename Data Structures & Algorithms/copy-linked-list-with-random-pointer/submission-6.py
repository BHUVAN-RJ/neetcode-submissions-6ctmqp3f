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
        if not head: return None
        nodes = {}
        curHead = head
        while curHead:
            nodes[curHead] = Node(curHead.val) 
            curHead = curHead.next
        
        newHead = nodes[head]
        while head:
            newNode = nodes[head]
            if head.random:
                newNode.random = nodes[head.random]
            
            if head.next:
                newNode.next = nodes[head.next]
            head = head.next

        
        return newHead
        