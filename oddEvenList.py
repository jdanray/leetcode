# https://leetcode.com/problems/odd-even-linked-list/

class Solution(object):
	def oddEvenList(self, head):
		if not head or not head.next:
			return head

		tail = [None, None]
		p = 1
		evenhead = head.next
		node = head
		while node:
			if tail[p]:
				tail[p].next = node
			tail[p] = node

			node = node.next
			p = 1 - p

		tail[0].next = None
		tail[1].next = evenhead

		return head
