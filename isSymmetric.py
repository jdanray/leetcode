# https://leetcode.com/problems/symmetric-tree/description/

class Solution(object):
	def isSymmetric(self, root):
		stack = [[root, root]]
		while stack:
			left, right = stack.pop()

			if not left and not right:
				continue
			elif not left or not right:
				return False
			elif left.val != right.val:
				return False

			stack.append([left.left, right.right])
			stack.append([left.right, right.left])

		return True
