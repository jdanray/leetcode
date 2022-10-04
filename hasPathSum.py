# https://leetcode.com/problems/path-sum/

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

class Solution(object):
	def hasPathSum(self, root, sum):
		if not root:
			return False

		if not root.left and not root.right:
			return root.val == sum

		return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
