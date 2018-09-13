# https://leetcode.com/problems/find-mode-in-binary-search-tree/description/

class Solution:
	def findMode(self, root):
		if not root:
			return []
		count = dict()
		stack = [root]
		while stack:
			node = stack.pop()
			if node:
				if node.val not in count:
					count[node.val] = 0
				count[node.val] += 1
				stack.append(node.left)
				stack.append(node.right)
		m = max(count.values())
		return [v for v in count if count[v] == m]
