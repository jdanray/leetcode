# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

class Solution(object):
	def insertGreatestCommonDivisors(self, head):
		node = head
		while node and node.next:
			d = math.gcd(node.val, node.next.val)
			i = ListNode(d)
			node.next, i.next = i, node.next
			node = i.next
		return head

class Solution(object):
	def insertGreatestCommonDivisors(self, head):
		if not head or not head.next:
			return head

		d = math.gcd(head.val, head.next.val)
		i = ListNode(d)
		head.next, i.next = i, head.next
		self.insertGreatestCommonDivisors(i.next)

		return head
