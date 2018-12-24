# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/

class Solution:
	def findTarget(self, root, k):
		values = []
		stack = [root]
		while stack:
			node = stack.pop()
			if node:
				stack.append(node.left)
				stack.append(node.right)
				values.append(node.val)

		for i in range(len(values)):
			for j in range(i + 1, len(values)):
				if values[i] + values[j] == k:
					return True

		return False
