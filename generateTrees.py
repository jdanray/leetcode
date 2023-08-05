# https://leetcode.com/problems/unique-binary-search-trees-ii/ 

class Solution(object):
	def generateTrees(self, n):
		def generate(l, r):
			if l > r:
				return [None]

			res = []
			for val in range(l, r + 1):
				for left in generate(l, val - 1):
					for right in generate(val + 1, r):
						node = TreeNode(val)
						node.left = left
						node.right = right
						res.append(node)

			return res 

		return generate(1, n)
