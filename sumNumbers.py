# https://leetcode.com/problems/sum-root-to-leaf-numbers/

class Solution:
	def sumNumbers(self, root):
		if not root:
			return 0

		total = 0
		stack = [[root, [root.val]]]
		while stack:
			node, digits = stack.pop()

			if not node.left and not node.right:
				place = 1
				s = 0
				for d in digits:
					s += d * place
					place *= 10
				total += s

			if node.left:
				stack.append([node.left, [node.left.val] + digits])

			if node.right:
				stack.append([node.right, [node.right.val] + digits])

		return total

class Solution(object):
	def sumNumbers(self, root):
		res = 0
		stack = [[root, 0]]
		while stack:
			node, num = stack.pop()

			if not node:
				continue

			num *= 10
			num += node.val

			if not node.left and not node.right:
				res += num

			stack.append([node.left, num])
			stack.append([node.right, num])

		return res
