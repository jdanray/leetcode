# https://leetcode.com/problems/find-bottom-left-tree-value/description/

class Solution:
	def findBottomLeftValue(self, root):
		leftmost = [root.val]
		depthmost = 0
		queue = [[leftmost, depthmost]]
		while queue:
			node, depth = queue.pop(0)
			if not node:
				continue
			if depth > depthmost:
				depthmost = depth:
				leftmost = node.val
			queue.append([node.left, depth + 1])
			queue.append([node.right, depth + 1])
		return leftmost
