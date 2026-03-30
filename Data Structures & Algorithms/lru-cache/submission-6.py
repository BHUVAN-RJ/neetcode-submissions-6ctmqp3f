class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def remove_node(self, node):
        print(node.value)
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def insert_node_at_end(self, node):
        self.tail.prev.next = node
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node

    def update_node(self, node):
        self.remove_node(node)
        self.insert_node_at_end(node)

    def get(self, key: int) -> int:
        print(self.cache)
        if key in self.cache:
            self.update_node(self.cache[key])
            return self.cache[key].value
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.update_node(self.cache[key])
            self.cache[key].value = value
        else:
            node = Node(key, value)
            self.insert_node_at_end(node)
            self.cache[key] = node
            print(len(self.cache), node.key,node.value)
            if len(self.cache) > self.capacity:
                del self.cache[self.head.next.key]
                self.remove_node(self.head.next)
        return

        
