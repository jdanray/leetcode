# https://leetcode.com/problems/subtree-of-another-tree/

class Solution:
	def isSub(self, s, t):
		if not s:
			return not t

		if not t:
			return False

		if s.val != t.val:
			return False

		return self.isSub(s.left, t.left) and self.isSub(s.right, t.right)

	def isSubtree(self, s, t):
		if self.isSub(s, t):
			return True

		return s and (self.isSubtree(s.left, t) or self.isSubtree(s.right, t))
