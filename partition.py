# https://leetcode.com/problems/partition-list/

class Solution(object):
	def partition(self, head, x):
		if not head:
			return None

		node = head
		heads = [None, None]	# [lt, gte]
		tails = [None, None]	# [lt, gte]
		while node:
			i = (node.val >= x)
			if not heads[i]:
				heads[i] = node
			if tails[i]:
				tails[i].next = node
			tails[i] = node
			node = node.next

		if tails[0]:
			if tails[1]:
				tails[1].next = None
			tails[0].next = heads[1]
			return heads[0]
		else:
			return heads[1]
