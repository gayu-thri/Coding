# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or head.next == None:
            return head 
        
        node1prev = odd = ListNode(0)
        node2prev = even = ListNode(0)
        count = 1
        temp = head
        while(temp):
            if count % 2 == 1:
                odd.next, odd = temp, temp
            else:
                even.next, even = temp, temp
            count = count + 1
            temp = temp.next
            
        even.next, odd.next = None, node2prev.next
        return node1prev.next