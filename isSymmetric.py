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

# New (recursive) solution:

class Solution(object):
	def isSymmetric(self, root):
		def helper(left, right):
			if left == None and right == None:
				return True
			elif left == None or right == None or left.val != right.val:
				return False

			return helper(left.left, right.right) and helper(left.right, right.left)

		return helper(root, root)
