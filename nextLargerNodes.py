# https://leetcode.com/problems/next-greater-node-in-linked-list/

class Solution:
	def nextLargerNodes(self, head):
		vals = []
		while head:
			vals.append(head.val)
			head = head.next

		stack = []
		res = []
		for i, v in enumerate(vals):
			while stack and stack[-1] < v:
				res[stack.pop()] = v
			stack.append(i)
			res.append(0)

		return res
