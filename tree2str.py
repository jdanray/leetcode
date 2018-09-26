# https://leetcode.com/problems/construct-string-from-binary-tree/description/

class Solution(object):
	def tree2str(self, root):
		if not root:
			return ""
		
		s = str(root.val)

		l = "(" + self.tree2str(root.left) + ")"
		r = "(" + self.tree2str(root.right) + ")"

		if root.right:
			s += l + r
		elif root.left:
			s += l

		return s
