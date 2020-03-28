# https://leetcode.com/problems/flip-equivalent-binary-trees/

class Solution(object):
	def flipEquiv(self, root1, root2):
		if not root1 and not root2:
			return True

		if root1 and not root2:
			return False

		if not root1 and root2:
			return False

		if root1.val != root2.val:
			return False

		if self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right):
			return True

		return self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
