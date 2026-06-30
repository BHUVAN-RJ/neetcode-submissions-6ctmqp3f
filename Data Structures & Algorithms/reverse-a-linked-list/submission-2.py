# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
# input: head for the normal LL
# output: head for the reversed LL
# goal : reverse the linked list
# 1 -> 2 -> 3 -> 4
# 1 <- 2 <- 3 <- 4(reversed)
# facts:
1. can have 0 elements
2. we are only given the head

assumptions are:
1. LL is always valid

approach:
 we get the cuurent -> cur
 go to next
 reverse it

 null <-1 <- 2 <- 3 <- 4  null
                  p    c.   h 

 cur = null
 while head
 prev = cur
 cur = head
 head = head.next
 cur.next = prev

 complesxity:
 O(n) -> go through all elements once
 O(1) -> no space aparte fmr the once already used
'''

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = None
        while head:
            prev = cur
            cur = head
            head = head.next
            cur.next = prev
        
        return cur


        