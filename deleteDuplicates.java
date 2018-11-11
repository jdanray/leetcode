// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

/*
 * I developed the algorithm in Python (see deleteDuplicates.py)
 * I translated the Python to Java to show prospective employers that I can write Java
 */

class Solution {
	public ListNode deleteDuplicates(ListNode head) {
		return deleteDuplicates(head, null);
	}

	public ListNode deleteDuplicates(ListNode head, ListNode prev) {
		if (head == null)
			return null;
		else if ((prev != null && prev.val == head.val) || (head.next != null && head.next.val == head.val))
			return deleteDuplicates(head.next, head);
		else {
			head.next = deleteDuplicates(head.next, head);
			return head;
		}
	}
}


/*
 * After I solve a problem, I like to study alternative solutions
 * The following program embodies a nifty way to approach the problem
 */

public ListNode deleteDuplicates(ListNode head) {
        if(head==null) return null;
        ListNode FakeHead=new ListNode(0);
        FakeHead.next=head;
        ListNode pre=FakeHead;
        ListNode cur=head;
        while(cur!=null){
            while(cur.next!=null&&cur.val==cur.next.val){
                cur=cur.next;
            }
            if(pre.next==cur){
                pre=pre.next;
            }
            else{
                pre.next=cur.next;
            }
            cur=cur.next;
        }
        return FakeHead.next;
    }
