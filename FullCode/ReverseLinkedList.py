# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        # 1 -> 2 -> 3 -> 4 -> 5 -> NULL
        # NULL <- 1 <- 2 <- 3 <- 4 <- 5 
        
        prev = None
        cur = head
        while cur != None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        head = prev
            
        return head
    
    def printlist(self, head):
        
        print('\nLinked list: ')
        temp = head
        while temp != None:
            print(temp.val," -> ",end="")
            temp = temp.next
        
s = Solution()
head = ListNode(1,ListNode(2))
head.next.next = ListNode(3,ListNode(4))
head.next.next.next.next = ListNode(5)

reversehead = s.reverseList(head)
print(s.printlist(reversehead))
