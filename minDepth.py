# https://leetcode.com/problems/minimum-depth-of-binary-tree/ 

class Solution(object):
	def minDepth(self, root):
		if not root:
			return 0

		mindepth = float('inf')
		stack = [[root, 1]]
		while stack:
			node, depth = stack.pop()

			if not node:
				continue

			if not node.left and not node.right:
				mindepth = min(mindepth, depth)

			stack.append([node.left, depth + 1])
			stack.append([node.right, depth + 1])

		return mindepth
