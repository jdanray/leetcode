# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/

class Solution:
	def findSecondMinimumValue(self, root):
		if not root:
			return -1
		values = set()
		stack = [root]
		while stack:
			node = stack.pop()
			if node:
				values.add(node.val)
				stack.append(node.left)
				stack.append(node.right)
		min1 = min(values)
		values.remove(min1)
		if not values:
			return -1
		return min(values)
