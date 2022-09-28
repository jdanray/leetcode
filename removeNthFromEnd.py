# https://leetcode.com/problems/remove-nth-node-from-end-of-list/ 

class Solution(object):
	def removeNthFromEnd(self, head, n):
		l = 0
		node = head
		while node:
			l += 1
			node = node.next

		k = l - n
		if k == 0:
			return head.next

		node = head
		while node:
			if k == 1 and node.next:
				node.next = node.next.next

			node = node.next
			k -= 1

		return head
