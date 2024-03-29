# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

class Solution(object):
	def largestValues(self, root):
		if not root:
			return []

		queue = [root]
		res = []
		while queue:
			maxim = float('-inf')
			for _ in range(len(queue)):
				node = queue.pop(0)
				maxim = max(maxim, node.val)

				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)

			res.append(maxim)

		return res

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

class Solution:
	def largestValues(self, root):
		if not root:
			return []

		values = []
		queue = [(0, root)]
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
