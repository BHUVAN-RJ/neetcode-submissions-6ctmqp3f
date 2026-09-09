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

        tmp = head
        while tmp:
            nodes[tmp] = Node(tmp.val)
            tmp = tmp.next
        
        tmp = head

        while tmp:
            cur_node = nodes[tmp]
            cur_node.next = nodes[tmp.next] if tmp.next else None
            cur_node.random = nodes[tmp.random] if tmp.random else None
            tmp = tmp.next
        
        return nodes[head] if head else None

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # nodes = {}
        # tmp = head
        # while tmp:
        #     nodes[tmp.val] = Node(tmp.val)
        #     tmp = tmp.next
        
        # tmp = head

        # while tmp:
        #     cur_node = nodes[tmp.val]
        #     cur_node.next = nodes[tmp.next.val] if tmp.next else None
        #     cur_node.random = nodes[tmp.random.val] if tmp.random else None
        #     tmp = tmp.next
        
        # return nodes[head.val] if head else None
        