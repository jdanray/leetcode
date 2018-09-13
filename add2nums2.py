# https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def lenList(self, l1):
		k = 0
		lst = l1
		while lst:
			k += 1
			lst = lst.next
		return k

	def numSize(self, num):
		k = 0
		while num > 0:
			k += 1
			num //= 10
		return k

	def toNum(self, l1):
		d = 10 ** (self.lenList(l1) - 1)
		n = 0
		lst = l1
		while lst:
			n += d * lst.val
			lst = lst.next
			d //= 10
		return n 

	def toList(self, num):
		if num == 0:
			return ListNode(0)
		s = self.numSize(num)
		d = 10 ** (s - 1)
		fakeHead = ListNode(1000)
		node = fakeHead
		for _ in range(s):
			k = num // d
			num -= (k * d)
			d //= 10
			node.next = ListNode(k)
			node = node.next
		return fakeHead.next

	def addTwoNumbers(self, l1, l2):
		s = self.toNum(l1) + self.toNum(l2)
		l = self.toList(s)
		return l
