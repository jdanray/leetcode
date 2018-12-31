# https://leetcode.com/problems/univalued-binary-tree/

class Solution(object):
	def isUnivalTree(self, root):
		stack = [root]
		seen = {root.val}
		while stack:
			node = stack.pop()

			if not node:
				continue

			if node.val not in seen:
				return False

			stack.append(node.left)
			stack.append(node.right)

		return True
