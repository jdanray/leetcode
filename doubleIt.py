# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/ 

class Solution(object):
	def doubleIt(self, head):
		node = head
		num = 0
		while node:
			num *= 10
			num += node.val
			node = node.next

		num *= 2
		numList = []
		while num > 0:
			numList.append(num % 10)
			num //= 10

		node = head
		while node and numList:
			n = numList.pop()
			node.val = n

			if not node.next and numList:
				node.next = ListNode(0)

			node = node.next

		return head
