# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

class Solution(object):
	def levelOrder(self, root):
		if not root:
			return []

		order = [[]]
		stack = [[root, 0]]
		curlevel = 0
		while stack:
			node, level = stack.pop()

			if not node:
				continue

			if level > curlevel:
				curlevel = level
				order.append([])

			order[-1].append(node)

			for child in node.children:
				stack.append([child, level + 1])

		return order
