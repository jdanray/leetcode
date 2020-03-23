# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

class Solution(object):
	def longestZigZag(self, root):
		res = 0
		stack = [[root, 0, 0]]
		while stack:
			node, direct, path = stack.pop()

			if not node:
				continue

			res = max(res, path)

			if direct == 0:
				stack.append([node.left, 0, 1])
				stack.append([node.right, 1, path + 1])
			else:
				stack.append([node.left, 0, path + 1])
				stack.append([node.right, 1, 1])

		return res 
