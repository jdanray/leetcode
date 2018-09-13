# https://leetcode.com/problems/trim-a-binary-search-tree/description/

class Solution:
	def trimBST(self, root, L, R):
		if not root:
			return None
		elif root.val < L:
			return self.trimBST(root.right, L, R)
		elif root.val > R:
			return self.trimBST(root.left, L, R)
		else:
			root.left = self.trimBST(root.left, L, R)
			root.right = self.trimBST(root.right, L, R)
			return root
