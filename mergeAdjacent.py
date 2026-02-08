# https://leetcode.com/problems/merge-adjacent-equal-elements/

class Solution(object):
	def mergeAdjacent(self, nums):
		stack = []
		for n in nums:
			while stack and stack[-1] == n:
				n += stack.pop()
			stack.append(n)
		return stack