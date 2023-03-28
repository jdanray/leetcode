# https://leetcode.com/problems/remove-linked-list-elements/

class Solution(object):
	def removeElements(self, head, val):
		fakeHead = ListNode(-1)
		fakeHead.next = head
		node = fakeHead
		while node: 
			while node.next and node.next.val == val:
				node.next = node.next.next
			node = node.next

		return fakeHead.next
