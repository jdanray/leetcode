# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

class Solution(object):
	def deleteMiddle(self, head):
		if not head.next:
			return None

		slow = head
		fast = head
		while fast.next and fast.next.next and fast.next.next.next:
			slow = slow.next
			fast = fast.next.next

		slow.next = slow.next.next
		return head
