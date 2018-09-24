# https://leetcode.com/problems/path-sum-ii/description/

class Solution:
	def pathSum(self, root, target):
		if not root:
			return []

		allpaths = []
		stack = [[root, [root.val]]]

		while stack:
			node, path = stack.pop()

			if not node.left and not node.right:
				if sum(path) == target:
					allpaths.append(path)
				continue

			if node.left:
				stack.append([node.left, path + [node.left.val]])
			if node.right:
				stack.append([node.right, path + [node.right.val]])

		return allpaths
