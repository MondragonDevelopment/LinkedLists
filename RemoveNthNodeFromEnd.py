"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
# O(N) Time | O(1) Space

from SinglyLinkedList import *


def removeNthFromEnd(head, n):
    counter = 1
    dummy = ListNode(0, head)
    first, second = dummy.next, dummy.next
    while counter <= n:
        second = second.next
        counter += 1
    if second is None:
        # print("I'm here")
        head.val = head.next.val        # Rewrites the head val (unless head.next is None) and
        head.next = head.next.next      # Make it point to the second val from it
        return 
    while second.next is not None:      # We stop with the second pointer pointing to null and the first one right before the Nth node from the end
        second = second.next
        first = first.next
    first.next = first.next.next
    return dummy.next

"""  

def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while n > 0 and right:
        right = right.next
        n -= 1
    
    while right:
        left = left.next
        right = right.next
    
    left.next = left.next.next
    return dummy.next
"""

heady = [1]
n = 1
linklist = LinkedList()

for node in heady:
    linklist.add(node)

linklist.print()

removeNthFromEnd(linklist.head, n)

linklist.print()
