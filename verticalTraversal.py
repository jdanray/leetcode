# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

class Solution(object):
	def verticalTraversal(self, root):
		if not root:
			return []

		vertical = {}
		stack = [[root, 0, 0]]
		while stack:
			node, x, y = stack.pop()

			if not node:
				continue

			vertical[x] = vertical.get(x, []) + [(y, node.val)]

			stack.append([node.left, x - 1, y + 1])
			stack.append([node.right, x + 1, y + 1])

		return [[val for y, val in sorted(vertical[x])] for x in sorted(vertical)]
