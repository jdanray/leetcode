# https://leetcode.com/problems/path-sum/description

class Solution(object):
	def hasPathSum(self, root, target):
		if not root:
			return False
		stack = [[root, root.val]]
		while stack:
			node, psum = stack.pop()
			if not node.left and not node.right:
				if psum == target:
					return True
				else:
					continue
			if node.left:
				stack.append([node.left, psum + node.left.val])
			if node.right:
				stack.append([node.right, psum + node.right.val])
		return False
