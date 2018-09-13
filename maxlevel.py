# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/

class Solution:
	def largestValues(self, root):
		if not root:
			return []
		queue = [(0, root)]
		values = []
		while queue:
			level, node = queue.pop(0)
			while level >= len(values):
				values.append([])
			values[level].append(node.val)
			if node.left:
				queue.append([level + 1, node.left])
			if node.right:
				queue.append([level + 1, node.right])
		return [max(v) for v in values]	
