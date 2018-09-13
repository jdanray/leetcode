# https://leetcode.com/problems/same-tree/description/

class Solution:
	def isSameTree(self, p, q):
		if p and q:
			return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
		return not p and not q
