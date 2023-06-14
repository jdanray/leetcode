# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

class Solution(object):
	def getMinimumDifference(self, root):
		nums = []
		stack = [root]
		while stack:
			node = stack.pop()

			if not node: 
				continue

			nums.append(node.val)

			stack.append(node.left)
			stack.append(node.right)

		nums = sorted(nums)
		res = float('inf')
		for i in range(1, len(nums)):
			res = min(res, nums[i] - nums[i - 1])

		return res
