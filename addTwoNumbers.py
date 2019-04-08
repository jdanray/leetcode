# https://leetcode.com/problems/add-two-numbers/

class Solution:
	def toNum(self, head):
		b = 1
		n = 0
		while head:
			n += b * head.val 
			b *= 10
			head = head.next
		return n

	def toList(self, num):
		head = ListNode(num % 10)
		num //= 10        
		if num > 0:
			head.next = self.toList(num)
		return head

	def addTwoNumbers(self, l1, l2):
		n1 = self.toNum(l1)
		n2 = self.toNum(l2)
		return self.toList(n1 + n2)
