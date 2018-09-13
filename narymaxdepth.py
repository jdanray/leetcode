# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/

class Solution(object):
	def maxDepth(self, root):
		if not root:
			return 0
		maxd = 1
		stack = [(root, maxd)]
		while stack:
			node, depth = stack.pop()
			if not node:
				continue
			maxd = max(depth, maxd)
			for child in node.children:
				stack.append((child, depth + 1))
		return maxd
