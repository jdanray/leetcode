# https://leetcode.com/problems/longest-univalue-path/

class Solution:
	def longestUnivaluePath(self, root):
		maxlen = 0
		stack = [[root, 0]]
		while stack:
			node, plen = stack.pop()
			if not node:
				continue

			if plen > maxlen:
				maxlen = plen

			if node.left and node.left.val == node.val:
				plen += 1
			if node.right and node.right.val == node.val:
				plen += 1

			if node.left and node.left.val == node.val:
				stack.append([node.left, plen])
			else:
				stack.append([node.left, 0])

			if node.right and node.right.val == node.val:
				stack.append([node.right, plen])
			else:
				stack.append([node.right, 0])

		return maxlen
