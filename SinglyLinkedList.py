class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, value):
        newNode = ListNode(value, None)

        if self.head is None:
            self.head = newNode
            return
        
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        lastNode = self.head
        llstr = ""

        while lastNode:
            llstr += str(lastNode.val) + "->"
            lastNode = lastNode.next
        print(llstr)
