# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

class Solution(object):
	def countPairs(self, root, distance):
		self.res = 0
		def dfs(root):
			if not root:
				return []

			if not root.left and not root.right:
				return [1]

			left = dfs(root.left)
			right = dfs(root.right)

			for l in left:
				for r in right:
					if l + r <= distance:
						self.res += 1

			return [l + 1 for l in left] + [r + 1 for r in right]

		dfs(root)
		return self.res
