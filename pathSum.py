# https://leetcode.com/problems/path-sum-ii/ 

class Solution(object):
	def pathSum(self, root, targetSum):
		if not root:
			return []

		res = []
		stack = [[root, root.val, [root.val]]]
		while stack:
			node, psum, path = stack.pop()

			if not node.left and not node.right:
				if psum == targetSum:
					res.append(path)
				continue

			if node.left:
				stack.append([node.left, psum + node.left.val, path + [node.left.val]])

			if node.right: 
				stack.append([node.right, psum + node.right.val, path + [node.right.val]])

		return res 
