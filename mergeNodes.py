# https://leetcode.com/problems/merge-nodes-in-between-zeros/ 

class Solution(object):
	def mergeNodes(self, head):
		left = head
		cur = head.next
		while cur:
			if cur.val == 0:
				if cur.next:
					left.next = cur
					left = cur
				else:
					left.next = None
			else:
				left.val += cur.val

			cur = cur.next

		return head
