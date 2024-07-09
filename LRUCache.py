"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
"""

"""
class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.cache = {}
        self.capacity = capacity or 1
        self.currentCapacity = 0
        self.listOfMostRecent = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.updateMostRecent(self.cache[key])
        return self.cache[key].value

    def put(self, key:int, value: int) -> None:
        if key not in self.cache:
            if self.currentCapacity == self.capacity:
                self.evictLeastRecent()
            else:
                self.currentCapacity += 1
            self.cache[key] = Node(key, value)
        else:
            self.replaceKey(key, value)
        self.updateMostRecent(self.cache[key])
    
    def replaceKey(self, key, value):
        if key not in self.cache:
            raise Exception("The provided key isn't in  the cache!")
        self.cache[key].value = value
    
    def updateMostRecent(self, node):
        self.listOfMostRecent.setHeadTo(node)
    
    def evictLeastRecent(self):
        keyToRemove = self.listOfMostRecent.tail.key
        self.listOfMostRecent.removeTail()
        del self.cache[keyToRemove]


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    
    def removeBindings(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(1) time | O(1) space
    def setHeadTo(self, node):
        if self.head == node:
            return
        elif self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.removeTail()
            node.removeBindings()
            self.head.prev = node
            node.next = self.head
            self.head = node

    def removeTail(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

"""

# Same LRU implementation but with a more friendly (simple and comprehensible) doublyLinkList implementation

class LRUCache:

    def __init__(self, capacity: int) -> None:
        self.cache = {}
        self.capacity = capacity
        self.currentCapacity = 0
        self.list = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.updateMostRecent(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key:int, value: int) -> None:
        if key not in self.cache:
            if self.currentCapacity == self.capacity:
                self.evictLeastRecent()
            else:
                self.currentCapacity += 1
            self.cache[key] = Node(key, value)
            self.list.insertNode(self.cache[key])
        else:
            self.replaceValue(key, value)
        
    def replaceValue(self, key, value):
        self.updateMostRecent(self.cache[key])
        self.cache[key].value = value
    
    def evictLeastRecent(self):
        keyToRemove = self.list.head.next.key
        self.list.removeNode(self.list.head.next)
        del self.cache[keyToRemove]
    
    def updateMostRecent(self, node):
        self.list.removeNode(node)
        self.list.insertNode(node)
    

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

# Here the most recent accessed Node will always be the tail.prev node

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head
    
    def insertNode(self, node):
        prev, nxt = self.tail.prev, self.tail
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
    
    def removeNode(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
