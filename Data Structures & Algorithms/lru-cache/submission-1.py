class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        self.right.prev = node
        node.next = self.right
        node.prev = prev
        print(self.right.val, self.left.val, self.left.next.val, self.right.prev.val)

    def get(self, key: int) -> int:
        print("GET", key)
        if key in self.cache:
            node = self.cache[key]
            print(node.val)
            self.remove(node)
            print("removed")
            self.insert(node)
            return node.val
        else: return -1
        

    def put(self, key: int, value: int) -> None:
        print("PUT", len(self.cache), self.capacity)
        if key in self.cache:
            print("KEY IN CACHE")
            node = self.cache[key]
            self.remove(node)
            del self.cache[key]
        elif len(self.cache) >= self.capacity:
            print("LEN GREATER PRUNING")
            del self.cache[self.left.next.key]
            self.remove(self.left.next)
        
        self.cache[key] = Node(key, value)
        
        self.insert(self.cache[key])
        
