class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
    
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def push(self, newval):
        new_node = Node(newval)
        new_node.next = self.head        
        self.head = new_node
        
    def print(self):
        temp = self.head
        while(temp != None):
            print(temp.val, end = "->")
            temp = temp.next
    
    def detectloop(self):
        slow = fast = self.head
        while(slow and fast and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return "There exists loop"
        return "There is no loop"
    
    def findmiddle(self):
        slow = fast = self.head
        while(fast and fast.next!=None):
            slow = slow.next
            fast = fast.next.next
        return slow
    
l = LinkedList()
l.push(5)
l.push(4)
l.push(3)
l.push(2)
l.push(1)

#l.head.next.next.next.next.next = l.head
#print(l.print())

print(l.detectloop())
print("The mid of linkedlist is: ", l.findmiddle().val)
        