# https://leetcode.com/problems/remove-linked-list-elements/

class Solution(object):
	def removeElements(self, head, val):
		fakeHead = ListNode(-1)
		fakeHead.next = head
		node = fakeHead
		while node:
			nxt = node.next
			while nxt and nxt.val == val:
				nxt = nxt.next
			node.next = nxt
			node = node.next

		return fakeHead.next
