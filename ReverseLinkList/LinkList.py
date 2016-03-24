
from Node import Node

class LinkList:
    def __init__(self, head=None):
        self.head = head;

    def addNode(self, next):
        if self.head is None:
            self.head = next;
            return

        current = self.head
        while current:
            if current.next is None:
                current.next = next
                break;
            current = current.next
        return

    def addData(self, data):
        self.addNode(Node(data))
        return

    def reverse(self):
        current = self.head
        next = None
        prev = None

        while (current):
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev    

    def dump(self):
        current = self.head
        while current:
            print "node: "+ current.data 
            current = current.next    
        return







                     

    
        
