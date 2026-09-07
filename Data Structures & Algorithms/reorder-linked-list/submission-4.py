# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
front[2,4,6,8,10]back
2->10->4->8->6

O(n) -> time
O(n) -> space


'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        tmp = head.next
        while tmp:
            nodes.append(tmp)
            tmp = tmp.next
        
        for node in nodes:
            print(node.val)
        
        front = 0
        back = len(nodes) - 1
        tmp = head
        use_front = False
        while front <= back:
            if use_front:
                print(tmp.val, nodes[front].val)
                tmp.next = nodes[front]
                front += 1
                use_front = False
            else:
                print(tmp.val, nodes[back].val)
                tmp.next = nodes[back]
                back -= 1
                use_front = True
            tmp = tmp.next
        tmp.next = None
        
        

