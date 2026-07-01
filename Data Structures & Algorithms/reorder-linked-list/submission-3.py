# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
INPUT: just head of the LL
OUTPUT: head of the reordered LL
GOAL: to reorder the list so that a list with n elements will be [0, n-1, 1, n-2... ]
in other words one element fromt he front and one element from the end.

dry run:
IP: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
                   t              h
1: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8. == len = 8 -> half 4 so reverse half the elements


2: 1 -> 2 -> 3 -> 4 <- 5 <- 6 <- 7 <- 8

3: 1 -> 2 -> 3 -> 4 <- 5 <- 6 <- 7 <- 8
                  h    t

                
res = 1 -> 8 -> 2 -> 7 -> 3 -> 6 -> 4 -> 5

REV-CASE_eve:
1 -> 2 -> 3 -> 4
     t         h

1 -> 2 <- 3 <- 4

CASE 2:
len = 5// 2 = 2
2 -> 4 -> 6 -> 8 -> 10 -> 11 -> 12 
               t                h

res = 2 -> 10 -> 4 -> 8 -> 6

facts:
will have atleast one item
we do not care what the node value is
we care is we have even or odd number of nodes
assumptions:

Ideas:
1. have two pointers - h and tail and take on from head and one from tail till h == t
 we need to always write head first ( for cases where len == odd)
 while front 
--> need the length
--> need to reverse the LL from the back
Solution
get LL length -> no need instead apply HT and get the middle directly
reverse till half 
apply the head and tail thing
the head == tail nothing but head and tail both exist
    ( in even case the next of mid will be null)
    ( in odd case write head, if tail == head skip thats it)

how to reverse?
we need tortoise and hare algo - so we can get mid

for even when hare is at the last second then it breaks and the tort is exactly in the center
and if it breaks at the end - then that means still in the middle - tortoise
even for ODD case - the tort will be in middle when hare is in end
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        cur = slow.next
        slow.next = None
        while cur:
            slow = cur
            cur = cur.next
            slow.next = prev
            prev = slow
        
        first, second = head, slow
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
            
            

            
        
        
        

        


        