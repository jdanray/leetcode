# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/

class Solution(object):
	def largestValues(self, root):
		maxima = []
		curlevel = 0
		queue = [[root, 1]]
		while queue:
			node, level = queue.pop(0)
			
			if not node:
				continue
			
			if level > curlevel:
				curlevel = level
				largest = node.val
				maxima.append(largest)

			if node.val > largest:
				largest = node.val
				maxima[curlevel] = largest

			queue.append([node.left, level + 1])
			queue.append([node.right, level + 1])

		return maxima
