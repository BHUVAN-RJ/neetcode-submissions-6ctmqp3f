class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}
        
    def remove_node(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def insert_node(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

    def update_node(self, node):
        self.remove_node(node)
        self.insert_node(node)

    def get(self, key: int) -> int:
        if key in self.cache:
            self.update_node(self.cache[key])
            return self.cache[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.update_node(self.cache[key])
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insert_node(node)
        if len(self.cache) > self.capacity:
            del self.cache[self.head.next.key]
            self.remove_node(self.head.next)
            


        
