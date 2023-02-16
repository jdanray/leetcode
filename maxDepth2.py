# https://leetcode.com/problems/maximum-depth-of-binary-tree/ 

class Solution(object):
	def maxDepth(self, root):
		if not root:
			return 0
		else:
			return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
