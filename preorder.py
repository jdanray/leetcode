# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

class Solution(object):
	def preorder(self, root):
		order = []
		stack = [root]
		while stack:
			node = stack.pop()
			if not node:
				continue

			order.append(node.val)

			for i in range(len(node.children) - 1, -1, -1):
				stack.append(node.children[i])

		return order
