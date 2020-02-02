# https://leetcode.com/problems/deepest-leaves-sum/ 

class Solution(object):
	def deepestLeavesSum(self, root):
		res = 0
		deepest = 0
		stack = [[root, 0]]
		while stack:
			node, depth = stack.pop()

			if not node:
				continue

			if not node.left and not node.right:
				if depth > deepest:
					deepest = depth
					res = node.val
				elif depth == deepest:
					res += node.val
			else:
				stack.append([node.left, depth + 1])
				stack.append([node.right, depth + 1])				

		return res
