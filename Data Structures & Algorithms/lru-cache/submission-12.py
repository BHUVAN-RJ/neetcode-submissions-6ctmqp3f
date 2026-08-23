class Node:
    def __init__(self,key=None, val=None, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev



class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.nodes = {}
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.nodes:
            node = self.nodes[key]
            self.remove_node(node)
            self.add_node(node)
            return node.val
        else:
            return -1
            

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.val = value
            self.remove_node(node)
            self.add_node(node)
        else:
            node = Node(key, value)
        
            self.nodes[key] = node
            if len(self.nodes) <= self.capacity:
                self.add_node(node)
            else:
                del self.nodes[self.tail.prev.key]
                self.remove_node(self.tail.prev)
                self.add_node(node)

    
    def add_node(self, node):
        tmp = self.head.next
        node.prev = self.head
        node.next = tmp
        self.head.next = node
        tmp.prev = node


    def remove_node(self, node):
        previous = node.prev
        next_element = node.next
        previous.next = next_element
        next_element.prev = previous
        node.next, node.prev = None, None

        
        
