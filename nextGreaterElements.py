# https://leetcode.com/problems/next-greater-element-ii/

class Solution:
	def nextGreaterElements(self, nums):
		res = [-1] * len(nums)
		stack = []
		for i in range(len(nums) * 2):
			n = nums[i % len(nums)]
			while stack and nums[stack[-1]] < n:
				res[stack.pop()] = n

			if i < len(nums):
				stack.append(i)

		return res
