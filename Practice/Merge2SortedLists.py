# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    result = temp = SinglyLinkedListNode(0)
    
    while head1 or head2:
        if head1 and (not head2 or head1.data < head2.data):
            temp.next = SinglyLinkedListNode(head1.data)
            head1 = head1.next if head1 else None
        else:
            temp.next = SinglyLinkedListNode(head2.data)
            head2 = head2.next if head2 else None
        
        temp = temp.next
    
    return result.next
        
        
            