# https://leetcode.com/problems/evaluate-boolean-binary-tree/

class Solution(object):
	def evaluateTree(self, root):
		if root.val == 2:
			return self.evaluateTree(root.left) | self.evaluateTree(root.right)
		elif root.val == 3:
			return self.evaluateTree(root.left) & self.evaluateTree(root.right)
		else:
			return root.val
