# https://leetcode.com/problems/most-frequent-subtree-sum/description/

class Solution:
	def findFrequentTreeSum(self, root):
		if not root:
			return []
		stack = [root]
		count = dict()
		while stack:
			node = stack.pop()
			if node:
				c = self.helper(node)
				if c not in count:
					count[c] = 0
				count[c] += 1
				stack.append(node.left)
				stack.append(node.right)
		m = max(count.values())
		return [c for c in count if count[c] == m]

	def helper(self, node):
		if not node:
			return 0
		else:
			return node.val + self.helper(node.left) + self.helper(node.right)
