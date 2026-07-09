class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyCircularQueue:

    def __init__(self, k: int):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left
        self.k = k
        self.length = k
        

    def enQueue(self, value: int) -> bool: # add an element to the left if space left!!
        # need to check if length is greater than 5 -> 4 -> 3 -> 2 -> 1 -> 0
        if self.isFull():
            return False
        
        tmp = self.right.prev
        node = Node(value)
        self.right.prev = node
        node.next = self.right
        node.prev = tmp
        tmp.next = node
        self.length -= 1 
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.length += 1
        return True

        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.val
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.val
        

    def isEmpty(self) -> bool:
        if self.length == self.k:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if self.length == 0:
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