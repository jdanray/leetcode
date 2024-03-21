# https://leetcode.com/problems/reverse-linked-list/ 

class Solution(object):
	def reverseList(self, head):
		newHead = None
		while head:
			nxt = head.next
			head.next = newHead
			newHead = head
			head = nxt

		return newHead

class Solution(object):
	def reverseList(self, head):
		def reverse(head, newHead):
			if head:
				nxt = head.next
				head.next = newHead
				return reverse(nxt, head)
			else:
				return newHead

		return reverse(head, None)

class Solution(object):
	def reverseList(self, head):
		if not head:
			return None

		prev = {}
		newHead = None
		node = head
		while node:
			newHead = node

			if node.next:
				prev[node.next] = node

			node = node.next

		for node in prev:
			node.next = prev[node]

		head.next = None
		return newHead
