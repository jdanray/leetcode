# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/

class Solution:
	def averageOfLevels(self, root):
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
		return [sum(v) / len(v) for v in values]	
