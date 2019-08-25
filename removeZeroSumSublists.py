# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

class Solution(object):
	def removeZeroSumSublists(self, head):
		if not head:
			return None

		s = head.val
		node = head.next
		while node and s != 0:
			s += node.val
			node = node.next

		if s == 0:
			return self.removeZeroSumSublists(node)

		head.next = self.removeZeroSumSublists(head.next)
		return head
