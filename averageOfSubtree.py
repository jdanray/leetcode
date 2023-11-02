# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/ 

class Solution(object):
	def averageOfSubtree(self, root):
		def helper(node):
			if not node:
				return (0, 0)

			ls, lc = helper(node.left)
			rs, rc = helper(node.right)

			s = ls + rs + node.val
			c = lc + rc + 1

			if node.val == s // c:
				self.res += 1

			return (s, c)

		self.res = 0
		helper(root)
		return self.res

class Solution(object):
	def averageOfSubtree(self, root):
		sumCount = {}
		def helper(node):
			if not node:
				return (0, 0)

			if node not in sumCount:
				ls, lc = helper(node.left)
				rs, rc = helper(node.right)
				sumCount[node] = (node.val + ls + rs, 1 + lc + rc)

			return sumCount[node]

		helper(root)
		return len([n for n in sumCount if n.val == sumCount[n][0] // sumCount[n][1]])
