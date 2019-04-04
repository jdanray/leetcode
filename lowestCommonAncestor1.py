# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

class Solution(object):
	def lowestCommonAncestor(self, root, p, q):
		if p.val < root.val and q.val < root.val:
			return self.lowestCommonAncestor(root.left, p, q)

		if p.val > root.val and q.val > root.val:
			return self.lowestCommonAncestor(root.right, p, q)

		return root
