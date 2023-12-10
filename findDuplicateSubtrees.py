# https://leetcode.com/problems/find-duplicate-subtrees/ 

class Solution(object):
	def findDuplicateSubtrees(self, root):
		def tree2str(root):
			if not root:
				return ''

			res = str(root.val)
			left = tree2str(root.left)
			right = tree2str(root.right)

			if left or right:
				res += '(' + left + ')'

			if right:
				res += '(' + right + ')'

			return res

		trees = collections.Counter()
		res = []
		def stringify(root):
			if root:
				s = tree2str(root)
				trees[s] += 1

				if trees[s] == 2:
					res.append(root)

				stringify(root.left)
				stringify(root.right)

		stringify(root)
		return res
