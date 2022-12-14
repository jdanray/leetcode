# https://leetcode.com/problems/house-robber-iii/

class Solution(object):
	def rob(self, root):
		memo = dict()
        
		def helper(root):
			if not root:
				return 0

			if root in memo:
				return memo[root]

			x = helper(root.left) + helper(root.right)
			y = root.val
			if root.left:
				y += helper(root.left.left) + helper(root.left.right)
			if root.right:
				y += helper(root.right.left) + helper(root.right.right)
		
			memo[root] = max(x, y)
			return memo[root]
        
		return helper(root)
