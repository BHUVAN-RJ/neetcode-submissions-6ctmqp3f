'''
len = 3
 (-->)H -> 1 -> 2 -> 3 -> T(-->)
 (<--)  <-   <-   <-   <-  (<--)   

'''
class Node:
    def __init__(self,val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.q = []
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            print("qfull")
            return False
        
        tmp = self.head.next
        node = Node(value)
        self.head.next = node
        node.next = tmp
        tmp.prev = node
        node.prev = self.head 
        self.q.append(value)
        
        return True
    
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.q.remove(self.tail.prev.val)
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        return True
        
        

    def Rear(self) -> int:
        print("rear",self.head.next.val)
        return -1 if self.isEmpty() else self.head.next.val
        

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.tail.prev.val
        

    def isEmpty(self) -> bool:
        if len(self.q) == 0:
            print('Q Empty')
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if len(self.q) == self.k:
            print(self.q, self.k)
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()