# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/ 

class Solution(object):
	def sumEvenGrandparent(self, root):
		if not root:
			return 0

		res = 0
		stack  = [[root, []]]
		while stack:
			node, parents = stack.pop()

			if not node:
				continue

			if len(parents) >= 2 and parents[-2] % 2 == 0:
				res += node.val

			stack.append([node.left, parents + [node.val]])
			stack.append([node.right, parents + [node.val]])

		return res
