"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Node:
    def __init__(self, x, next = None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        nodes = {}
        curNode = head
        while curNode:
            nodes[curNode] = Node(curNode.val)
            curNode = curNode.next
        
        for node in nodes:
            nextNode = node.next
            random = node.random
            newCurNode = nodes[node]
            newCurNode.next = nodes[nextNode] if nextNode else None
            newCurNode.random = nodes[random] if random else None
        
        return nodes[head]