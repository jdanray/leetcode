# https://leetcode.com/contest/weekly-contest-110/problems/range-sum-of-bst/

class Solution(object):
	def rangeSumBST(self, root, L, R):
		if not root:
			return 0
		elif root.val >= L and root.val <= R:
			return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
		elif root.val < L:
			return self.rangeSumBST(root.right, L, R)
		elif root.val > R:
			return self.rangeSumBST(root.left, L, R)
