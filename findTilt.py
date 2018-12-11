# https://leetcode.com/problems/binary-tree-tilt/

class Solution(object):
	def findTilt(self, root):
		self.tilt = 0

		def computeTilt(root):
			if not root:
				return 0

			leftsum = 0
			rightsum = 0
			if root.left:
				leftsum = root.left.val + computeTilt(root.left)
			if root.right:
				rightsum = root.right.val + computeTilt(root.right)

			self.tilt += abs(leftsum - rightsum)
			return leftsum + rightsum

		computeTilt(root)
		return self.tilt

"""
After I solve a problem, I like to examine solutions that other people have come up with.
The following is a slightly simpler version of my solution.
"""

class Solution(object):
	def findTilt(self, root):
		self.tilt = 0
		def computeTilt(root):
			if not root:
				return 0

			leftsum = computeTilt(root.left)
			rightsum = computeTilt(root.right)

			self.tilt += abs(leftsum - rightsum)
			return leftsum + rightsum + root.val

		computeTilt(root)
		return self.tilt
