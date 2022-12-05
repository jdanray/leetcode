# https://leetcode.com/contest/weekly-contest-95/problems/middle-of-the-linked-list/

class Solution(object):
	def middleNode(self, head):
		n = 0
		h = head
		while h:
			n += 1
			h = h.next

		for _ in range(n // 2):
			head = head.next

		return head

class Solution(object):
	def middleNode(self, head):
		slow = head
		fast = head
		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next
		return slow
