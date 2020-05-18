# https://leetcode.com/problems/count-good-nodes-in-binary-tree/ 

class Solution(object):
	def goodNodes(self, root, maxi=None):
		if not root:
			return 0

		if maxi == None or root.val >= maxi:
			return 1 + self.goodNodes(root.left, root.val) + self.goodNodes(root.right, root.val)

		return self.goodNodes(root.left, maxi) + self.goodNodes(root.right, maxi)
