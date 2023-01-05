# https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/ 

class Solution(object):
	def minDeletion(self, nums):
		stack = []
		res = 0
		for n in nums:
			while stack and stack[-1] == n and len(stack) % 2 == 1:
				stack.pop()
				res += 1

			stack.append(n)

		if len(stack) % 2 == 1:
			res += 1

		return res
