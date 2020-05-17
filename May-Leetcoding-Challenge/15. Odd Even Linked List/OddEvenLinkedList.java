/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode oddEvenList(ListNode head) 
    {
        if (head == null || head.next == null) 
		    return head;
	
        ListNode node1prev = new ListNode(0);
        ListNode node2prev = new ListNode(0);
        ListNode odd = node1prev;
        ListNode even = node2prev;
        
        int count = 1;
        ListNode temp = head;
        
        while(temp != null)
        {
            if(count % 2 == 1)
            {
                odd.next= temp;
                odd = temp;
            }
            else
            {
                even.next= temp;
                even = temp;
            }
            count += 1;
            temp = temp.next;
        }
        even.next = null;
        odd.next = node2prev.next;
        return node1prev.next;    
    }
}