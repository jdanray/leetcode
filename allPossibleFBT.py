# https://leetcode.com/problems/all-possible-full-binary-trees/ 

class Solution(object):
	def allPossibleFBT(self, n):
		if n % 2 == 0:
			return []

		if n == 1:
			return [TreeNode(0)]

		res = []
		for i in range(1, n, 2):
			left = self.allPossibleFBT(i)
			right = self.allPossibleFBT(n - i - 1)

			for l in left:
				for r in right:
					root = TreeNode(0)
					root.left = l
					root.right = r

					res += [root]

		return res
