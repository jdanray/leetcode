# https://leetcode.com/problems/swap-nodes-in-pairs/ 

class Solution(object):
	def swapPairs(self, head):
		if not head or not head.next:
			return head

		newHead = head.next
		head.next = self.swapPairs(head.next.next)
		newHead.next = head

		return newHead
