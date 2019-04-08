# https://leetcode.com/problems/add-two-numbers-ii/

class Solution(object):
	def length(self, head):
		l = 0
		while head:
			l += 1
			head = head.next
		return l

	def toNum(self, head):
		b = 10 ** (self.length(head) - 1)
		n = 0
		while head:
			n += b * head.val
			b //= 10
			head = head.next
		return n

	def toList(self, num):
		if num == 0:
			return ListNode(0)

		head = None
		tail = None
		while num > 0:
			head = ListNode(num % 10)
			head.next = tail
			tail = head
			num //= 10
		return head

	def addTwoNumbers(self, l1, l2):
		n1 = self.toNum(l1)
		n2 = self.toNum(l2)
		return self.toList(n1 + n2)
