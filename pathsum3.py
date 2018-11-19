# https://leetcode.com/problems/path-sum-iii/description/

class Solution(object):
	def pathSum(self, root, target):
		stack = [[root, []]]
		npaths = 0
		while stack:
			node, pathsums = stack.pop()
			
			if not node:
				continue

			pathsums = [node.val + p for p in pathsums] + [node.val]
			npaths += len([p for p in pathsums if p == target])

			stack.append([node.left, pathsums])
			stack.append([node.right, pathsums])

		return npaths
