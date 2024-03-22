# https://leetcode.com/problems/reverse-nodes-in-even-length-groups/ 

class Solution(object):
	def reverseEvenLengthGroups(self, head):
		n = 0
		node = head
		while node:
			n += 1
			node = node.next

		i = 0
		group = 1
		prev = None
		node = head
		while node:
			l = min(group, n - i)

			if l % 2 == 0:
				newHead = None
				origHead = node
				for _ in range(l):
					nxt = node.next
					node.next = newHead
					newHead = node
					node = nxt
					i += 1
				prev.next = newHead
				origHead.next = nxt
				prev = origHead
			else:
				for _ in range(l):
					prev = node
					node = node.next
					i += 1

			group += 1

		return head

class Solution(object):
	def reverseEvenLengthGroups(self, head):
		n = 0
		node = head
		while node:
			n += 1
			node = node.next

		i = 0
		group = 1
		prev = None
		node = head
		while node:
			l = min(group, n - i)

			newHead = None
			origHead = node
			for _ in range(l):
				nxt = node.next

				if l % 2 == 0:
					node.next = newHead

				newHead = node
				node = nxt
				i += 1

			if l % 2 == 0:
				prev.next = newHead
				origHead.next = nxt
				prev = origHead
			else:
				prev = newHead

			group += 1

		return head
