# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
IN: head of LL
OUT: head of LL
Goal: remove the Nth element from the end frmo the LL

facts: N will always == or  < size

solution:
we have two pointers but move the first n spaces from the slow initially so that 
we have the n gap and then move both at the same pace so when we reach the end we will also 
have the element n spaces behiend

DRY run:
D -> 1 -> 2 -> 3 -> 4.   || n = 2
p    q
diff = 1

1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9  || n = 5
               p                        q


D ->5
p   q
diff = 1
'''

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        diff = 1
        dummy = ListNode(0, head)
        p1, p2 = dummy, dummy.next
        while diff < n:
            diff += 1
            p2 = p2.next
        

        while p2.next:
            p1 = p1.next
            p2 = p2.next
        
        p1.next = p1.next.next

        return dummy.next
        